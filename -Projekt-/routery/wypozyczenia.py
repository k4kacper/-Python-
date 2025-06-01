from fastapi import APIRouter, HTTPException
from modele.wypozyczenie import Wypozyczenie
from baza.baza_falszywych import wypozyczenia_db, ksiazki_db
from pydantic import BaseModel, EmailStr
from datetime import datetime

router = APIRouter()
id_counter = 1

# Model dla żądania wypożyczenia
class WypozyczRequest(BaseModel):
    nazwaKsiazki: str
    emailUzytkownika: EmailStr

# Model dla żądania zwrotu
class ZwrotRequest(BaseModel):
    nazwa_ksiazki: str
    email_uzytkownika: EmailStr

# Funkcja pomocnicza do znajdowania książki
def znajdz_ksiazke(nazwaKsiazki: str):
    return next((ksiazka for ksiazka in ksiazki_db if ksiazka.tytul.lower() == nazwaKsiazki.lower()), None)

# Funkcja pomocnicza do znajdowania wypożyczenia
def znajdz_wypozyczenie(wypozyczenie_id: int):
    return next((wypozyczenie for wypozyczenie in wypozyczenia_db if wypozyczenie.id == wypozyczenie_id), None)

def znajdz_aktywne_wypozyczenie(nazwa_ksiazki: str, email_uzytkownika: str):
    return next(
        (w for w in wypozyczenia_db
         if w.nazwaKsiazki.lower() == nazwa_ksiazki.lower()
         and w.emailUzytkownika.lower() == email_uzytkownika.lower()
         and not w.return_date),
        None
    )

@router.post("/wypozycz/")
def wypozycz_ksiazke(request: WypozyczRequest):
    global id_counter

    ksiazka = znajdz_ksiazke(request.nazwaKsiazki)

    if not ksiazka:
        raise HTTPException(404, "Książka nie istnieje")

    if not ksiazka.dostepna:
        raise HTTPException(400, "Książka już wypożyczona")

    wypozyczenie = Wypozyczenie(
        id=id_counter,
        nazwaKsiazki=request.nazwaKsiazki,
        emailUzytkownika=request.emailUzytkownika,
        wypozyczono_date=datetime.now(),
        return_date=None
    )

    ksiazka.dostepna = False
    wypozyczenia_db.append(wypozyczenie)
    id_counter += 1

    return {"wiadomosc": "Książka wypożyczona!", "wypozyczenie": wypozyczenie}


@router.put("/zwroc/")
def zwroc_ksiazke(request: ZwrotRequest):
    # Znajdź aktywne wypożyczenie
    wypozyczenie = znajdz_aktywne_wypozyczenie(request.nazwa_ksiazki, request.email_uzytkownika)

    if not wypozyczenie:
        raise HTTPException(status_code=404,
                            detail="Nie znaleziono aktywnego wypożyczenia dla tej książki i użytkownika")

    # Znajdź książkę i oznacz jako dostępną
    ksiazka = znajdz_ksiazke(request.nazwa_ksiazki)
    if ksiazka:
        ksiazka.dostepna = True

    # Ustaw datę zwrotu
    wypozyczenie.return_date = datetime.now()

    return {"wiadomosc": "📖 Książka zwrócona!", "wypozyczenie": wypozyczenie}


@router.get("/historia/{emailUzytkownika}")
def historia_wypozyczen(emailUzytkownika: EmailStr):
    historia = [wyp for wyp in wypozyczenia_db if wyp.emailUzytkownika.lower() == emailUzytkownika.lower()]
    return {"wiadomosc": "Historia wypożyczeń", "historia": historia}