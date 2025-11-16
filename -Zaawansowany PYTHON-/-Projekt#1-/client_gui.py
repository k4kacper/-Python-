import socket, threading, json, time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog, messagebox

HOST_DEFAULT = "127.0.0.1"
PORT_DEFAULT = 9999

class ModernBankClient:
    def __init__(self, root):
        self.root = root
        root.title("💳 Prosty Bank — Klient")
        root.geometry("1420x710")
        self.sock = None
        self.buffer = ""
        style = ttk.Style("superhero")
        frm = ttk.Frame(root, padding=(12,12))
        frm.pack(fill=BOTH, expand=1)
        top_row = ttk.Frame(frm)
        top_row.pack(fill=X, pady=(0,8))
        ttk.Label(top_row, text="Serwer:", width=8).pack(side=LEFT)
        self.host = ttk.Entry(top_row, width=18)
        self.host.insert(0, HOST_DEFAULT)
        self.host.pack(side=LEFT, padx=(0,8))
        ttk.Label(top_row, text="Port:", width=6).pack(side=LEFT)
        self.port = ttk.Entry(top_row, width=7)
        self.port.insert(0, str(PORT_DEFAULT))
        self.port.pack(side=LEFT, padx=(0,12))
        ttk.Label(top_row, text="Użytkownik:", width=12).pack(side=LEFT)
        self.user = ttk.Entry(top_row, width=16)
        self.user.pack(side=LEFT, padx=(0,8))
        ttk.Label(top_row, text="Hasło:", width=6).pack(side=LEFT)
        self.pwd = ttk.Entry(top_row, width=14, show="*")
        self.pwd.pack(side=LEFT, padx=(0,8))
        btn_row = ttk.Frame(frm)
        btn_row.pack(fill=X, pady=(0,8))
        self.connect_btn = ttk.Button(btn_row, text="🔗 Połącz i zaloguj", bootstyle=(SUCCESS, "outline"), command=self.connect_login)
        self.connect_btn.pack(side=LEFT, padx=6, ipadx=6)
        self.logout_btn = ttk.Button(btn_row, text="🚪 Wyloguj", bootstyle=(DANGER, "outline"), command=self.logout, state=DISABLED)
        self.logout_btn.pack(side=LEFT, padx=6, ipadx=6)
        ttk.Separator(frm).pack(fill=X, pady=8)
        mid = ttk.Frame(frm)
        mid.pack(fill=BOTH, expand=1)
        left = ttk.Frame(mid)
        left.pack(side=LEFT, fill=BOTH, expand=1, padx=(0,8))
        right = ttk.Frame(mid, width=260)
        right.pack(side=RIGHT, fill=Y)
        actions = ttk.Labelframe(left, text="Akcje", padding=8)
        actions.pack(fill=X)
        ttk.Button(actions, text="💰 Saldo", bootstyle=INFO, command=self.balance).pack(side=LEFT, padx=6, pady=6, ipadx=8)
        ttk.Button(actions, text="👥 Lista użytkowników", bootstyle=INFO, command=self.list_users).pack(side=LEFT, padx=6, pady=6, ipadx=8)
        ttk.Button(actions, text="💸 Przelew", bootstyle=INFO, command=self.transfer).pack(side=LEFT, padx=6, pady=6, ipadx=8)
        log_frame = ttk.Labelframe(left, text="Log", padding=8)
        log_frame.pack(fill=BOTH, expand=1, pady=(8,0))
        self.log = ttk.Text(log_frame, height=16, wrap="word", borderwidth=0)
        self.log.pack(fill=BOTH, expand=1)
        self.status = ttk.Label(frm, text="Niepołączony", bootstyle=SECONDARY)
        self.status.pack(fill=X, pady=(8,0))
        right_lbl = ttk.Label(right, text="Ostatnia lista użytkowników", anchor="w")
        right_lbl.pack(fill=X, pady=(0,6), padx=6)
        cols = ("username","balance")
        self.users_tree = ttk.Treeview(right, columns=cols, show="headings", height=16)
        self.users_tree.heading("username", text="Użytkownik")
        self.users_tree.heading("balance", text="Saldo")
        self.users_tree.column("username", anchor="w", width=140)
        self.users_tree.column("balance", anchor="e", width=90)
        self.users_tree.pack(fill=BOTH, expand=1, padx=6, pady=(0,6))
        style.configure("Treeview", rowheight=26)
        frm.columnconfigure(0, weight=1)
        frm.rowconfigure(3, weight=1)

    def connect_login(self):
        if self.sock:
            self._log("Już połączony.")
            return
        host = self.host.get().strip()
        try:
            port = int(self.port.get().strip())
        except:
            messagebox.showerror("Błąd", "Nieprawidłowy port")
            return
        user = self.user.get().strip()
        pwd = self.pwd.get().strip()
        if not user or not pwd:
            messagebox.showwarning("Brak danych", "Podaj użytkownika i hasło.")
            return
        try:
            s = socket.create_connection((host, port), timeout=8)
            s.settimeout(None)
            self.sock = s
            threading.Thread(target=self.recv_loop, daemon=True).start()
            self._send({"action":"login","username":user,"password":pwd})
            self._log(f"Łączenie z {host}:{port} jako {user}...")
            self.status.config(text="Łączenie...", bootstyle=SECONDARY)
        except Exception as e:
            messagebox.showerror("Błąd połączenia", str(e))
            self._log(f"Błąd połączenia: {e}")

    def logout(self):
        if self.sock:
            try: self._send({"action":"logout"})
            except: pass
            try: self.sock.close()
            except: pass
        self.sock = None
        self.connect_btn.config(state=NORMAL)
        self.logout_btn.config(state=DISABLED)
        self.status.config(text="Rozłączony", bootstyle=DANGER)
        self._log("Rozłączono.")

    def recv_loop(self):
        try:
            while self.sock:
                data = self.sock.recv(4096)
                if not data:
                    self._queue_info("Serwer zamknął połączenie")
                    break
                self.buffer += data.decode("utf-8", errors="replace")
                while "\n" in self.buffer:
                    line, self.buffer = self.buffer.split("\n", 1)
                    if line.strip():
                        self.root.after(0, lambda l=line: self.handle_msg(l))
        except Exception as e:
            self._queue_info(f"Błąd odbioru: {repr(e)}")
        finally:
            self.sock = None
            self.root.after(0, lambda: (self.connect_btn.config(state=NORMAL), self.logout_btn.config(state=DISABLED), self.status.config(text="Rozłączony", bootstyle=DANGER)))

    def _send(self, obj):
        data = json.dumps(obj, ensure_ascii=False) + "\n"
        try:
            self.sock.sendall(data.encode("utf-8"))
        except Exception as e:
            self._log(f"Send error: {e}")

    def handle_msg(self, line):
        try:
            msg = json.loads(line)
        except Exception:
            self._log("Niepoprawny JSON: " + line)
            return
        t = msg.get("type")
        if t == "welcome":
            self._log("[SERWER] " + msg.get("message", ""))
        elif t == "login_ok":
            self._log("✅ Zalogowano: " + msg.get("message", ""))
            self.status.config(text=f"Zalogowany ({msg.get('balance','?')})", bootstyle=SUCCESS)
            self.connect_btn.config(state=DISABLED)
            self.logout_btn.config(state=NORMAL)
        elif t == "login_failed":
            self._log("❌ Logowanie nieudane: " + msg.get("message",""))
            self.status.config(text="Logowanie nieudane", bootstyle=DANGER)
        elif t == "balance":
            self._log(f"💰 Saldo: {msg.get('balance')}")
        elif t == "users":
            users = msg.get("users",[])
            self._update_users_list(users)
            users_str = "\n".join([f"{u['username']} — {u['balance']}" for u in users])
            self._log("👥 Użytkownicy:\n" + users_str)
        elif t == "transfer_ok":
            self._log(f"💸 Przelew OK: {msg.get('message')}")
            self.status.config(text=f"Saldo: {msg.get('balance','?')}", bootstyle=SUCCESS)
        elif t == "notification":
            self._log("🔔 " + msg.get("message",""))
        elif t == "error":
            self._log("⚠️ " + msg.get("message",""))
        elif t == "logout_ok":
            self._log("🚪 Wylogowano")
            self.status.config(text="Wylogowany", bootstyle=INFO)
            self.connect_btn.config(state=NORMAL)
            self.logout_btn.config(state=DISABLED)
        else:
            self._log("[INNE] " + json.dumps(msg, ensure_ascii=False))

    def balance(self):
        if self.sock: self._send({"action":"balance"})

    def list_users(self):
        if self.sock: self._send({"action":"list_users"})

    def transfer(self):
        if not self.sock: return
        to = simpledialog.askstring("Przelew", "Do kogo (username)?", parent=self.root)
        if not to: return
        amt = simpledialog.askstring("Kwota", "Podaj kwotę:", parent=self.root)
        if not amt: return
        try:
            float(amt)
        except:
            messagebox.showerror("Błąd", "Nieprawidłowa kwota")
            return
        self._send({"action":"transfer", "to":to, "amount":amt})
        self._log(f"Wysłano: przelew → {to}: {amt}")

    def _update_users_list(self, users):
        for iid in self.users_tree.get_children():
            self.users_tree.delete(iid)
        for u in users:
            uname = u.get("username","?")
            bal = u.get("balance","?")
            self.users_tree.insert("", "end", values=(uname, f"{bal}"))

    def _log(self, text):
        ts = time.strftime("%H:%M:%S")
        self.log.insert("end", f"{ts} — {text}\n")
        self.log.see("end")

    def _queue_info(self, text):
        self.root.after(0, lambda: self._log(text))

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    ModernBankClient(root)
    root.mainloop()
