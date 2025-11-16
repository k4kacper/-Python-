#!/usr/bin/env python3
"""
server.py - prosty, stabilny serwer TCP JSON (newline-delimited)
Kompatybilny z client_gui_clean.py (akcje: login, balance, list_users, transfer, logout).
- Host: 0.0.0.0
- Port: 9999
- Prosta in-memory DB z kilkoma kontami demo
- Współbieżność: wątek na klienta + lock do DB i listy połączeń
- Obsługa fragmentowanych wiadomości (buffer + split by '\n')
"""

import socket
import threading
import json
import traceback

HOST = "0.0.0.0"
PORT = 9999

db_lock = threading.Lock()
clients_lock = threading.Lock()

# In-memory DB: username -> {password, balance}
users_db = {
    "alice": {"password": "alice123", "balance": 1000.0},
    "bob":   {"password": "bobpass",   "balance": 500.0},
    "carol": {"password": "carolpw",   "balance": 750.0},
}

# connected clients: list of dicts {conn, addr, username}
connected_clients = []

# helper: wysyłka JSON z newline
def send_json(conn, obj):
    try:
        data = json.dumps(obj, ensure_ascii=False) + "\n"
        conn.sendall(data.encode("utf-8"))
    except Exception:
        # ignore send errors quietly
        pass

def broadcast_notification(message, exclude_conn=None):
    """Wyślij powiadomienie 'notification' do wszystkich zalogowanych klientów,
       opcjonalnie pomijając exclude_conn (np. nadawcę)."""
    with clients_lock:
        for c in connected_clients:
            if c.get("username") and c["conn"] is not exclude_conn:
                send_json(c["conn"], {"type": "notification", "message": message})

def handle_client(conn, addr):
    client = {"conn": conn, "addr": addr, "username": None}
    with clients_lock:
        connected_clients.append(client)

    try:
        # powitanie od razu po połączeniu
        send_json(conn, {"type": "welcome", "message": "Witaj w prostym serwerze bankowym. Zaloguj się (action:'login')."})

        buffer = ""
        while True:
            data = conn.recv(4096)
            if not data:
                # połączenie zamknięte przez klienta
                break
            buffer += data.decode("utf-8", errors="replace")
            # przetwarzaj pełne linie zakończone '\n'
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    req = json.loads(line)
                except json.JSONDecodeError:
                    send_json(conn, {"type":"error", "message":"Nieprawidłowy JSON"})
                    continue

                action = req.get("action", "").lower()

                # LOGIN
                if action == "login":
                    username = req.get("username")
                    password = req.get("password")
                    if not username or not password:
                        send_json(conn, {"type":"login_failed", "message":"Brakuje nazwy użytkownika lub hasła"})
                        continue
                    with db_lock:
                        user = users_db.get(username)
                        if user and user.get("password") == password:
                            client["username"] = username
                            send_json(conn, {"type":"login_ok", "message": f"Zalogowano jako {username}", "balance": user["balance"]})
                            broadcast_notification(f"Użytkownik {username} się zalogował.", exclude_conn=conn)
                        else:
                            send_json(conn, {"type":"login_failed", "message":"Nieprawidłowy login lub hasło"})
                # BALANCE
                elif action == "balance":
                    if not client.get("username"):
                        send_json(conn, {"type":"error", "message":"Nie jesteś zalogowany"})
                        continue
                    with db_lock:
                        bal = users_db[client["username"]]["balance"]
                    send_json(conn, {"type":"balance", "balance": bal})
                # LIST USERS
                elif action == "list_users":
                    if not client.get("username"):
                        send_json(conn, {"type":"error", "message":"Nie jesteś zalogowany"})
                        continue
                    with db_lock:
                        lst = [{"username": u, "balance": users_db[u]["balance"]} for u in users_db]
                    send_json(conn, {"type":"users", "users": lst})
                # TRANSFER
                elif action == "transfer":
                    if not client.get("username"):
                        send_json(conn, {"type":"error", "message":"Nie jesteś zalogowany"})
                        continue
                    to_user = req.get("to")
                    amount = req.get("amount")
                    if to_user is None or amount is None:
                        send_json(conn, {"type":"error", "message":"Brakuje danych (to/amount)"})
                        continue
                    try:
                        amount = float(amount)
                    except Exception:
                        send_json(conn, {"type":"error", "message":"Nieprawidłowa kwota"})
                        continue
                    if amount <= 0:
                        send_json(conn, {"type":"error", "message":"Kwota musi być większa niż 0"})
                        continue
                    with db_lock:
                        sender = users_db.get(client["username"])
                        receiver = users_db.get(to_user)
                        if not receiver:
                            send_json(conn, {"type":"error", "message":"Odbiorca nie istnieje"})
                            continue
                        if sender["balance"] < amount:
                            send_json(conn, {"type":"error", "message":"Niewystarczające środki"})
                            continue
                        # wykonaj przelew
                        sender["balance"] -= amount
                        receiver["balance"] += amount
                        sender_balance = sender["balance"]
                    # potwierdzenie nadawcy
                    send_json(conn, {"type":"transfer_ok", "message": f"Przelew do {to_user} wykonany", "balance": sender_balance})
                    # powiadom innych (wyślij także do odbiorcy jeśli zalogowany)
                    broadcast_notification(f"{client['username']} przelał {amount:.2f} do {to_user}.", exclude_conn=None)
                # LOGOUT
                elif action == "logout":
                    if client.get("username"):
                        name = client["username"]
                        client["username"] = None
                        send_json(conn, {"type":"logout_ok", "message":"Wylogowano"})
                        broadcast_notification(f"Użytkownik {name} się wylogował.", exclude_conn=None)
                    else:
                        send_json(conn, {"type":"error", "message":"Nie byłeś zalogowany"})
                else:
                    send_json(conn, {"type":"error", "message":"Nieznana akcja"})
    except Exception as e:
        # logujemy wyjątek na serwerze, klient dostanie tylko komunikat o zerwaniu połączenia
        print("Błąd w wątku klienta:", e)
        traceback.print_exc()
    finally:
        # cleanup
        with clients_lock:
            if client in connected_clients:
                connected_clients.remove(client)
        if client.get("username"):
            broadcast_notification(f"Użytkownik {client['username']} rozłączył się.", exclude_conn=None)
        try:
            conn.close()
        except Exception:
            pass
        print("Połączenie zamknięte:", addr)

def main():
    print(f"Start serwera na {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(50)
        try:
            while True:
                conn, addr = s.accept()
                print("Nowe połączenie od", addr)
                t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
                t.start()
        except KeyboardInterrupt:
            print("Zatrzymywanie serwera...")

if __name__ == "__main__":
    main()
