import uvicorn
from fastapi import FastAPI
from routery import ksiazki, uzytkownicy, wypozyczenia

app = FastAPI()

app.include_router(ksiazki.router, prefix="/ksiazki", tags=["ksiazki"])
app.include_router(uzytkownicy.router, prefix="/uzytkownicy", tags=["uzytkownicy"])
app.include_router(wypozyczenia.router, prefix="/wypozyczenia", tags=["wypozyczenia"])

@app.get("/")
def home():
    return {"wiadomosc": "Witaj w systemie zarządzania biblioteką!"}

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8080, reload=True)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)