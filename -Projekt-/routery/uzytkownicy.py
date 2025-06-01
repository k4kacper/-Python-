from fastapi import APIRouter, HTTPException
from modele.uzytkownik import Uzytkownik
from baza.baza_falszywych import uzytkownicy_db

router = APIRouter()

@router.post("/")
def dodaj_uzytkownika(uzytkownik: Uzytkownik):
    if any(u.email == uzytkownik.email for u in uzytkownicy_db):
        raise HTTPException(status_code=400, detail="E-mail już istnieje!")

    uzytkownicy_db.append(uzytkownik)
    return {"wiadomosc": "Użytkownik dodany!", "uzytkownik": uzytkownik}

@router.get("/")
def pobierz_uzytkownikow():
    return uzytkownicy_db

@router.delete("/{id}")
def usun_uzytkownika(id: int):
    global uzytkownicy_db
    uzytkownik_do_usuniecia = next((u for u in uzytkownicy_db if u.id == id), None)

    if not uzytkownik_do_usuniecia:
        raise HTTPException(status_code=404, detail="Użytkownik nie istnieje")

    uzytkownicy_db = [u for u in uzytkownicy_db if u.id != id]
    return {"wiadomosc": "Użytkownik usunięty!", "id": id}

@router.put("/{id}")
def edytuj_uzytkownika(id: int, nowy_uzytkownik: Uzytkownik):
    global uzytkownicy_db
    for i, u in enumerate(uzytkownicy_db):
        if u.id == id:
            uzytkownicy_db[i] = nowy_uzytkownik
            return {"wiadomosc": "Użytkownik zaktualizowany!", "uzytkownik": nowy_uzytkownik}

    raise HTTPException(status_code=404, detail="Użytkownik nie istnieje")