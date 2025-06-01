from fastapi import APIRouter, HTTPException, Query
from modele.ksiazka import Ksiazka
from baza.baza_falszywych import ksiazki_db

router = APIRouter()

@router.post("/")
def dodaj_ksiazke(ksiazka: Ksiazka):
    ksiazki_db.append(ksiazka)
    return {"wiadomosc": "Książka dodana", "ksiazka": ksiazka}

@router.get("/")
def pobierz_ksiazki():
    return ksiazki_db

@router.delete("/usun/")
def usun_ksiazke(nazwa_ksiazki: str = Query(..., description="Nazwa książki do usunięcia")):
    global ksiazki_db

    # Znajdź książkę do usunięcia
    ksiazka_do_usuniecia = next((k for k in ksiazki_db if k.tytul.lower() == nazwa_ksiazki.lower()), None)

    if not ksiazka_do_usuniecia:
        raise HTTPException(status_code=404, detail="Nie znaleziono książki o podanym tytule")

    # Sprawdź czy książka nie jest wypożyczona
    if not ksiazka_do_usuniecia.dostepna:
        raise HTTPException(status_code=400, detail="Nie można usunąć wypożyczonej książki")

    # Usuń książkę z listy
    ksiazki_db = [k for k in ksiazki_db if k.tytul.lower() != nazwa_ksiazki.lower()]

    return {"wiadomosc": f"📖 Książka '{nazwa_ksiazki}' została usunięta!"}



@router.get("/szukaj/")
def szukaj_ksiazki(tytul: str = Query(None), autor: str = Query(None)):
    wyniki = ksiazki_db

    if tytul:
        wyniki = [ksiazka for ksiazka in wyniki if tytul.lower() in ksiazka.tytul.lower()]
    if autor:
        wyniki = [ksiazka for ksiazka in wyniki if autor.lower() in ksiazka.autor.lower()]

    return wyniki

