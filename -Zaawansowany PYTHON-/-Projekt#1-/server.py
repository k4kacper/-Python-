from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import threading
from typing import Dict, List

app = FastAPI()

# — Prosta baza w pamięci (reset przy restarcie) —
db_lock = threading.Lock()
users_db: Dict[str, Dict] = {
    "alice": {"password": "alice123", "balance": 1000.0},
    "bob":   {"password": "bobpass",   "balance": 500.0},
    "carol": {"password": "carolpw",   "balance": 750.0},
}

# -- websocket manager (broadcast powiadomień) —
class ConnectionManager:
    def __init__(self):
        self.active: List[WebSocket] = []
        self.lock = threading.Lock()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        with self.lock:
            self.active.append(websocket)

    def disconnect(self, websocket: WebSocket):
        with self.lock:
            if websocket in self.active:
                self.active.remove(websocket)

    async def broadcast(self, message: dict):
        with self.lock:
            conns = list(self.active)
        for ws in conns:
            try:
                await ws.send_json(message)
            except Exception:
                # jeśli wysyłka nie powiodła się, odłączamy w kolejnym kroku
                pass

ws_manager = ConnectionManager()

# -- Modele requestów --
class LoginRequest(BaseModel):
    username: str
    password: str

class TransferRequest(BaseModel):
    from_user: str
    to: str
    amount: float

# -- Endpoints API --
@app.post("/api/login")
def login(req: LoginRequest):
    with db_lock:
        user = users_db.get(req.username)
        if not user or user.get("password") != req.password:
            raise HTTPException(status_code=401, detail="Nieprawidłowy login lub hasło")
        return {"username": req.username, "balance": user["balance"]}

@app.get("/api/balance/{username}")
def balance(username: str):
    with db_lock:
        user = users_db.get(username)
        if not user:
            raise HTTPException(status_code=404, detail="Użytkownik nie znaleziony")
        return {"username": username, "balance": user["balance"]}

@app.get("/api/users")
def list_users():
    with db_lock:
        return [{"username": u, "balance": users_db[u]["balance"]} for u in users_db]

@app.post("/api/transfer")
async def transfer(req: TransferRequest):
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Kwota musi być większa niż 0")
    with db_lock:
        sender = users_db.get(req.from_user)
        receiver = users_db.get(req.to)
        if not sender:
            raise HTTPException(status_code=404, detail="Nadawca nie istnieje")
        if not receiver:
            raise HTTPException(status_code=404, detail="Odbiorca nie istnieje")
        if sender["balance"] < req.amount:
            raise HTTPException(status_code=400, detail="Niewystarczające środki")
        sender["balance"] -= req.amount
        receiver["balance"] += req.amount
        new_balance = sender["balance"]

    # Broadcast powiadomienia do wszystkich podłączonych websocketów
    await ws_manager.broadcast({
        "type": "notification",
        "message": f"{req.from_user} przelał {req.amount:.2f} do {req.to}",
        "from": req.from_user,
        "to": req.to,
        "amount": req.amount
    })

    return {"status": "ok", "balance": new_balance}

# — websocket endpoint dla powiadomień —
@app.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_json({"type": "pong", "echo": data})
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
    except Exception:
        ws_manager.disconnect(websocket)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="127.0.0.1",
        port=9090,
        reload=True
    )