"""ZADANIA PROSTE"""
"""Klasa Prostokąt (Rectangle):
Utwórz klasę reprezentującą prostokąt z atrybutami długości i szerokości. Klasa powinna zawierać metody do obliczania obwodu i pola powierzchni oraz metodę do zmiany wymiarów prostokąta."""

class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

    def pole(self):
        return self.dlugosc * self.szerokosc

    def zmien_wymiary(self, nowa_dlugosc, nowa_szerokosc):
        self.dlugosc = nowa_dlugosc
        self.szerokosc = nowa_szerokosc


"""Klasa Student:
Stwórz klasę dla studenta z atrybutami imię, nazwisko, numer indeksu oraz lista ocen. Dodaj metody do wyświetlania danych studenta, aktualizacji numeru indeksu oraz obliczania średniej ocen."""

class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, oceny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny if oceny else []

    def wyswietl_dane(self):
        return f"{self.imie} {self.nazwisko}, Indeks: {self.numer_indeksu}, Oceny: {self.oceny}"

    def aktualizuj_indeks(self, nowy_indeks):
        self.numer_indeksu = nowy_indeks

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny) if self.oceny else 0


"""Klasa Konto Bankowe (BankAccount):
Zaprojektuj klasę dla konta bankowego z atrybutami saldo, numer konta, oraz historia transakcji. Dodaj metody do wpłaty, wypłaty, sprawdzania salda oraz wyświetlania historii transakcji."""

class KontoBankowe:
    def __init__(self, numer_konta, saldo=0):
        self.numer_konta = numer_konta
        self.saldo = saldo
        self.historia_transakcji = []

    def wplata(self, kwota):
        self.saldo += kwota
        self.historia_transakcji.append(f"Wplata: {kwota}")

    def wyplata(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            self.historia_transakcji.append(f"Wyplata: {kwota}")
        else:
            print("Brak wystarczajacych srodkow.")

    def sprawdz_saldo(self):
        return self.saldo

    def pokaz_historie_transakcji(self):
        return self.historia_transakcji


"""Klasa Książka (Book):
Utwórz klasę dla książki z atrybutami tytuł, autor, liczba stron oraz dostępność. Dodaj metody do wyświetlania informacji o książce, aktualizacji dostępności oraz wypożyczania i zwracania książki."""

class Ksiazka:
    def __init__(self, tytul, autor, liczba_stron, dostepnosc=True):
        self.tytul = tytul
        self.autor = autor
        self.liczba_stron = liczba_stron
        self.dostepnosc = dostepnosc

    def wyswietl_info(self):
        return f"Tytul: {self.tytul}, Autor: {self.autor}, Strony: {self.liczba_stron}, Dostepnosc: {self.dostepnosc}"

    def wypozycz(self):
        if self.dostepnosc:
            self.dostepnosc = False
        else:
            print("Ksiazka jest niedostepna.")

    def zwroc(self):
        self.dostepnosc = True


"""Klasa Pies (Dog):
Stwórz klasę reprezentującą psa z atrybutami rasa, wiek, imię oraz zdrowie. Dodaj metody do szczekania, przedstawiania psa oraz aktualizacji stanu zdrowia."""

class Pies:
    def __init__(self, rasa, wiek, imie, zdrowie="Zdrowy"):
        self.rasa = rasa
        self.wiek = wiek
        self.imie = imie
        self.zdrowie = zdrowie

    @staticmethod
    def szczekaj():
        return "Hau! Hau!"

    def przedstaw(self):
        return f"{self.imie}, {self.wiek}-letni {self.rasa}. Stan zdrowia: {self.zdrowie}"

    def aktualizuj_zdrowie(self, status):
        self.zdrowie = status


"""Klasa Kalkulator (Calculator):
Zaprojektuj klasę kalkulatora z metodami do dodawania, odejmowania, mnożenia, dzielenia dwóch liczb oraz zapisywania ostatniego wyniku i wyświetlania historii operacji."""

class Kalkulator:
    def __init__(self):
        self.historie = []

    def dodaj(self, a, b):
        wynik = a + b
        self.historie.append(f"Dodawanie: {wynik}")
        return wynik

    def odejmij(self, a, b):
        wynik = a - b
        self.historie.append(f"Odejmowanie: {wynik}")
        return wynik

    def mnoz(self, a, b):
        wynik = a * b
        self.historie.append(f"Mnozenie: {wynik}")
        return wynik

    def dziel(self, a, b):
        if b == 0:
            return "Nie mozna dzielic przez zero!"
        wynik = a / b
        self.historie.append(f"Dzielenie: {wynik}")
        return wynik

    def pokaz_historie(self):
        return self.historie


"""Klasa Film (Movie):
Utwórz klasę dla filmu z atrybutami tytuł, gatunek, rok wydania oraz ocena. Dodaj metody do wyświetlania pełnej informacji o filmie, zmiany oceny oraz porównywania filmów na podstawie ocen."""

class Film:
    def __init__(self, tytul, gatunek, rok_wydania, ocena):
        self.tytul = tytul
        self.gatunek = gatunek
        self.rok_wydania = rok_wydania
        self.ocena = ocena

    def wyswietl_info(self):
        return f"Tytul: {self.tytul}, Gatunek: {self.gatunek}, Rok: {self.rok_wydania}, Ocena: {self.ocena}"

    def zmien_ocene(self, nowa_ocena):
        self.ocena = nowa_ocena


"""Klasa Produkt (Product):
Stwórz klasę reprezentującą produkt z atrybutami nazwa, cena, ilość w magazynie oraz kategoria. Dodaj metody do aktualizacji ceny i ilości, wyświetlania informacji o produkcie oraz filtrowania produktów według kategorii."""

class Produkt:
    def __init__(self, nazwa, cena, ilosc, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc
        self.kategoria = kategoria

    def aktualizuj_cene(self, nowa_cena):
        self.cena = nowa_cena

    def aktualizuj_ilosc(self, nowa_ilosc):
        self.ilosc = nowa_ilosc

    def wyswietl_info(self):
        return f"Produkt: {self.nazwa}, Cena: {self.cena}, Ilosc: {self.ilosc}, Kategoria: {self.kategoria}"


"""Klasa Zegar (Clock):
Utwórz klasę zegara z atrybutami godzin, minut, sekund oraz format (AM/PM lub 24-godzinny). Dodaj metody do wyświetlania aktualnego czasu, zmiany formatu oraz ustawiania nowego czasu."""

class Zegar:
    def __init__(self, godziny, minuty, sekundy, format_24=True):
        self.godziny = godziny
        self.minuty = minuty
        self.sekundy = sekundy
        self.format_24 = format_24

    def wyswietl_czas(self):
        return f"{self.godziny:02}:{self.minuty:02}:{self.sekundy:02}" + (" AM/PM" if not self.format_24 else "")

    def zmien_format(self):
        self.format_24 = not self.format_24


"""Klasa Pociąg (Train):
Zaprojektuj klasę dla pociągu z atrybutami numer pociągu, liczba wagonów oraz lista pasażerów. Dodaj metody do wyświetlania informacji o pociągu, dodawania i usuwania pasażerów oraz obliczania całkowitej liczby pasażerów."""

class Pociag:
    def __init__(self, numer, liczba_wagonow):
        self.numer = numer
        self.liczba_wagonow = liczba_wagonow
        self.pasazerowie = []

    def dodaj_pasazera(self, pasazer):
        self.pasazerowie.append(pasazer)

    def usun_pasazera(self, pasazer):
        if pasazer in self.pasazerowie:
            self.pasazerowie.remove(pasazer)

    def liczba_pasazerow(self):
        return len(self.pasazerowie)

    def wyswietl_info(self):
        return f"Pociag nr {self.numer}, Wagony: {self.liczba_wagonow}, Pasazerowie: {self.liczba_pasazerow()}"


# Prostokat
prostokat = Prostokat(10, 5)
print(prostokat.obwod())  # 30
print(prostokat.pole())  # 50
prostokat.zmien_wymiary(8, 4)
print(prostokat.obwod())  # 24

# Student
student = Student("Jan", "Kowalski", "123456", [5, 4, 3, 5])
print(student.wyswietl_dane())
print(student.srednia_ocen())  # 4.25
student.aktualizuj_indeks("654321")
print(student.wyswietl_dane())

# Konto Bankowe
konto = KontoBankowe("987654321")
konto.wplata(500)
konto.wyplata(200)
print(konto.sprawdz_saldo())  # 300
print(konto.pokaz_historie_transakcji())

# Ksiazka
ksiazka = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 400)
print(ksiazka.wyswietl_info())
ksiazka.wypozycz()
print(ksiazka.wyswietl_info())
ksiazka.zwroc()
print(ksiazka.wyswietl_info())

# Pies
pies = Pies("Labrador", 3, "Max")
print(pies.szczekaj())
print(pies.przedstaw())
pies.aktualizuj_zdrowie("Chory")
print(pies.przedstaw())

# Kalkulator
kalkulator = Kalkulator()
print(kalkulator.dodaj(5, 3))  # 8
print(kalkulator.odejmij(10, 4))  # 6
print(kalkulator.pokaz_historie())

# Film
film = Film("Incepcja", "Sci-Fi", 2010, 9)
print(film.wyswietl_info())
film.zmien_ocene(10)
print(film.wyswietl_info())

# Produkt
produkt = Produkt("Laptop", 3000, 10, "Elektronika")
print(produkt.wyswietl_info())
produkt.aktualizuj_cene(2800)
print(produkt.wyswietl_info())

# Zegar
zegar = Zegar(14, 30, 45)
print(zegar.wyswietl_czas())
zegar.zmien_format()
print(zegar.wyswietl_czas())

# Pociag
pociag = Pociag("IC123", 8)
pociag.dodaj_pasazera("Anna Nowak")
print(pociag.wyswietl_info())
pociag.usun_pasazera("Anna Nowak")
print(pociag.wyswietl_info())