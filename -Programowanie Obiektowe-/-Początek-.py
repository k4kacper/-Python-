print("-----------------------------------------------------------------------------\n")
"""1. Klasa `Samochód`: Zdefiniuj klasę `Samochód` z atrybutami `marka`, `model`,
`rok` i `przebieg`, a następnie utwórz kilka obiektów reprezentujących różne
samochody"""

class Samochod:
    def __init__(self, marka, model, rok, przebieg):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.przebieg = przebieg

mercedes = Samochod("Mercedes", "C63 AMG", "2009", "14000")
print(mercedes.marka, mercedes.model, mercedes.rok, mercedes.przebieg)
audi = Samochod("Audi", "A8L", "2021", "26700")
print(audi.marka, audi.model, audi.rok, audi.przebieg)
bmw = Samochod("BMW", "M4 G82", "2025", "1000")
print(bmw.marka, bmw.model, bmw.rok, bmw.przebieg)

print("\n-----------------------------------------------------------------------------\n")
"""2. Klasa `Prostokąt`: Napisz klasę `Prostokąt` z atrybutami `szerokość` i `wysokość`
oraz metodami `pole()` i `obwód()` do obliczania pola powierzchni i obwodu
prostokąta."""

class Prostokat:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc

    def obwod(self):
        return (2 * self.szerokosc) + (2 * self.wysokosc)

prostokat = Prostokat(5, 10)
print("Pole prostokątu wynosi:", prostokat.pole())
print("Obwód prostokątu wynosi:", prostokat.obwod())

print("\n-----------------------------------------------------------------------------\n")
"""3. Klasa `Koło`: Utwórz klasę `Koło` z atrybutem `promień` oraz metodami `pole()` i
`obwód()`, które obliczają odpowiednio pole powierzchni i obwód koła."""

class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return 3.14 * pow(self.promien, 2)

    def obwod(self):
        return 2 * 3.14 * self.promien

kolo = Kolo(3)
print("Pole koła wynosi: ", kolo.pole())
print("Obwód koła wynosi: ", kolo.obwod())

print("\n-----------------------------------------------------------------------------\n")
"""4. Klasa `KontoBankowe`: Stwórz klasę `KontoBankowe` z atrybutami `numer_konta`,
`właściciel`, `saldo` oraz metodami `wplata()` i `wyplata()` do zarządzania
operacjami na koncie."""

class KontoBankowe:
    def __init__(self, numer_konta, wlasciciel, saldo):
        self.numer_konta = numer_konta
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplata(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            print(f"Wpłata {kwota} zł zakończona sukcesem. Aktualne saldo: {self.saldo} zł.")
        else:
            print("Kwota wpłaty musi być większa od zera.")

    def wyplata(self, kwota):
        if 0 < kwota <= self.saldo:
            self.saldo -= kwota
            print(f"Wypłata {kwota} zł zakończona sukcesem. Aktualne saldo: {self.saldo} zł.")
        elif kwota > self.saldo:
            print("Niewystarczające środki na koncie.")
        else:
            print("Kwota wypłaty musi być większa od zera.")


konto = KontoBankowe(1, "Andrzej", 100)
print("Saldo przed wpłatą:", konto.saldo)
konto.wplata(250)
print("Saldo po wpłacie:", konto.saldo)
print("Saldo przed wypłatą:", konto.saldo)
konto.wyplata(65)
print("Saldo po wypłacie:", konto.saldo)

print("\n-----------------------------------------------------------------------------\n")
"""5. Klasa `Uczeń`:Utwórz klasę `Uczeń` z atrybutami `imię`, `nazwisko`, `klasa` oraz
`oceny` (jako lista), oraz metodą `średnia_ocen()` obliczającą średnią ocen ucznia."""

class Uczen:
    def __init__(self, imie, nazwisko, klasa, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        self.oceny = oceny

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny)

uczen = Uczen("Jan", "Kowalski", "8C", [4,6,3,2,4.5])
print("Średnia ocen wynosi:", uczen.srednia_ocen())

print("\n-----------------------------------------------------------------------------\n")
"""6. Klasa `Książka`: Zdefiniuj klasę `Książka` z atrybutami `tytuł`, `autor`,
`rok_wydania`, `ilość_stron`, oraz metodą `opis()`, która wyświetla całkowity opis
książki."""

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, ilosc_stron):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.ilosc_stron = ilosc_stron

    def opis(self):
        print(f"Książka ma tytuł {self.tytul}, autorem jest {self.autor}, książka została wydana w {self.rok_wydania} roku, posiada ona {self.ilosc_stron} stron.")

ksiazka = Ksiazka("Krótka piłka", "Coben", 2018, 325)
ksiazka.opis()

print("\n-----------------------------------------------------------------------------\n")
"""7. Klasa `Zwierzę`: Napisz klasę `Zwierzę` z atrybutami `gatunek` i `wiek`. Utwórz
podklasy `Pies` i `Kot`, które będą dziedziczyć z klasy `Zwierzę`, dodając metody
specyficzne dla każdego gatunku."""

class Zwierze:
    def __init__(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek

class Pies(Zwierze):
    def __init__(self, gatunek, wiek):
        super().__init__(gatunek, wiek)

    @staticmethod
    def dzwiek():
        print("HAU!")

class Kot(Zwierze):
    def __init__(self, gatunek, wiek):
        super().__init__(gatunek, wiek)

    @staticmethod
    def dzwiek():
        print("MIAU!")

pies = Pies("Labrador", 6)
kot = Kot("Brytyjczyk", 3)
print(f"Pies jest rasy {pies.gatunek} i ma {pies.wiek} lat.")
pies.dzwiek()
print(f"Kot jest rasy {kot.gatunek} i ma {kot.wiek} lat.")
kot.dzwiek()

print("\n-----------------------------------------------------------------------------\n")
"""8. Klasa `Osoba`: Zbuduj klasę `Osoba` z atrybutami `imię` i `nazwisko` oraz
metodami `przedstaw_się()`, które będą wyświetlać pełne imię i nazwisko osoby."""

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Cześć nazywam się {self.nazwisko} {self.imie}.")

osoba = Osoba("Grzegorz", "Maciaszek")
osoba.przedstaw_sie()

print("\n-----------------------------------------------------------------------------\n")
"""9. Klasa `Film`: Utwórz klasę `Film` z atrybutami `tytuł`, `reżyser`, `rok_produkcji`,
oraz metodą `opis()`, która wyświetla pełny opis filmu."""

class Film:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji

    def opis(self):
        print(f"Film pt. ''{self.tytul}'', którego reżyserem jest {self.rezyser}, został wyreżyserowany w {self.rok_produkcji} roku.")

film = Film("Furia", "David Ayer", 2014)
film.opis()

print("\n-----------------------------------------------------------------------------\n")
"""10. Klasa `Rachunek`: Napisz klasę `Rachunek` z atrybutami `numer`, `właściciel`,
`kwota` oraz metodami `dodaj_transakcję()` i `wyświetl_rachunek()` do zarządzania
transakcjami na rachunku."""

class Rachunek:
    def __init__(self, numer, wlasciciel, kwota):
        self.numer= numer
        self.wlasciciel = wlasciciel
        self.kwota = kwota
        self.transakcje = []

    def dodaj_transakcje(self, opis, kwota):
        if kwota != 0:
            self.transakcje.append({"opis": opis, "kwota": kwota})
            self.kwota += kwota
            print(f"Transakcja dodana: {opis} | Kwota: {kwota} zł. Aktualne saldo: {self.kwota} zł.")
        else:
            print("Kwota transakcji nie może być równa zeru.")

    def wyswietl_rachunek(self):
        print(f"Rachunek numer: {self.numer}")
        print(f"Właściciel: {self.wlasciciel}")
        print(f"Saldo: {self.kwota} zł")
        print("Historia transakcji:")
        for transakcja in self.transakcje:
            print(f" - {transakcja['opis']}: {transakcja['kwota']} zł")

rachunek = Rachunek("987654321", "Kacper Nowak", 1000)
rachunek.dodaj_transakcje("Wpłata początkowa", 500)
rachunek.dodaj_transakcje("Zakupy spożywcze", -200)
rachunek.dodaj_transakcje("Wynagrodzenie", 3000)
rachunek.wyswietl_rachunek()

print("\n-----------------------------------------------------------------------------\n")
"""11. Klasa `Gra`: Utwórz klasę `Gra` z atrybutami `nazwa`, `gatunek`, `wydawca`,
oraz metodą `opis()`, która wyświetla szczegóły gry."""

class Gra:
    def __init__(self, nazwa, gatunek, wydawca):
        self.nazwa = nazwa
        self.gatunek = gatunek
        self.wydawca = wydawca

    def opis(self):
        print(f"Gra {self.nazwa}, która pochodzi z gatunku {self.gatunek}, której wydawcą jest: {self.wydawca}")

gra = Gra("Rainbow Six Siege", "First Person Shooter", "Ubisoft")
gra.opis()

print("\n-----------------------------------------------------------------------------\n")
"""12. Klasa `Zegarek`: Napisz klasę `Zegarek` z atrybutami `marka`, `model`, oraz
metodą `pokaz_czas()`, która będzie drukować aktualny czas."""
import time
class Zegarek:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    @staticmethod
    def pokaz_czas():
        t = time.localtime()
        czas = time.strftime("%H:%M:%S", t)
        print(f"Obecny czas to {czas}")

zegarek = Zegarek("Rolex", "Submariner")
zegarek.pokaz_czas()

print("\n-----------------------------------------------------------------------------\n")
"""13. Klasa `Wehikuł`:Stwórz klasę `Wehikuł` z atrybutami `typ`,
`prędkość_maksymalna`, oraz metodą `przesun()` symulującą ruch wehikułu"""

class Wehikul:
    def __init__(self, typ, predkosc_maksymalna):
        self.typ = typ
        self.predkosc_maksymalna = predkosc_maksymalna

    def przesun(self, dystans):
        czas = dystans / self.predkosc_maksymalna
        print(f"Wehikuł typu {self.typ} przemieszcza się na odległość {dystans} km. Szacowany czas: {czas:.2f} godz.")

wehikul = Wehikul("Rakieta", 3000)
wehikul.przesun(2400)

print("\n-----------------------------------------------------------------------------\n")
"""14. Klasa `Pracownik`:Utwórz klasę `Pracownik` z atrybutami `imię`, `nazwisko`,
`stanowisko`, `pensja`, oraz metodą `opis_pracownika()`, która wyświetla pełne
informacje o pracowniku."""

class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja

    def opis_pracownik(self):
        print(f"{self.imie} {self.nazwisko} jest pracownikiem na stanowisku {self.stanowisko} oraz otrzymuje pensje w wysokości {self.pensja} zł")

pracownik = Pracownik("Andrzej", "Ból", "Sprzedawca", "6500")
pracownik.opis_pracownik()

print('\n-----------------------------------------------------------------------------\n')
"""15. Klasa `Biblioteka`: Zdefiniuj klasę `Biblioteka` z atrybutem `książki` (jako lista) i
metodą `dodaj_książkę()` do dodawania książek do biblioteki oraz `wyświetl_książki()`
do pokazania wszystkich książek."""

class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, tytul_ksiazki):
        self.ksiazki.append(tytul_ksiazki)

    def wyswietl_ksiazki(self):
        print("Książki w bibliotece:")
        for ksiazki in self.ksiazki:
            print(f"- {ksiazki}")

biblioteka = Biblioteka()
biblioteka.dodaj_ksiazke("Harry Poter")
biblioteka.dodaj_ksiazke("Potop")
biblioteka.dodaj_ksiazke("Lalka")
biblioteka.wyswietl_ksiazki()

print("\n-----------------------------------------------------------------------------\n")
"""16. Klasa `Hotel`:Napisz klasę `Hotel` z atrybutami `nazwa`, `adres`, `ilość_pokoi`,
oraz metodą `zarezerwuj_pokój()` obsługującą rezerwacje."""

class Hotel:
    def __init__(self, nazwa, adres, ilosc_pokoi):
        self.nazwa = nazwa
        self.adres = adres
        self.ilosc_pokoi = ilosc_pokoi

    def zarezerwuj_pokoj(self):
        print(f"Rezerwacja w hotelu {self.nazwa}, który znajduje się na {self.adres}, łącznie zarezerwowano {self.ilosc_pokoi} pokój/pokoje/pokoi")

hotel = Hotel("Athena", "ul.Paderewskiego Warszawa", 2)
hotel.zarezerwuj_pokoj()

print("\n-----------------------------------------------------------------------------\n")
"""17. Klasa `Klient`: Utwórz klasę `Klient` z atrybutami `imię`, `nazwisko`, `adres`,
oraz metodą `wyświetl_dane()` do wyświetlania pełnych danych klienta."""

class Klient:
    def __init__(self, imie, nazwisko, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

    def wyswietl_dane(self):
        print(f"Klient nazywa się {self.imie} {self.nazwisko} i mieszka w {self.adres}")

klient = Klient("Maciek", "Mazur", "Gdańsku ul.Erwina 12")
klient.wyswietl_dane()

print("\n-----------------------------------------------------------------------------\n")
"""18. Klasa `Kalkulator`: Stwórz klasę `Kalkulator` z metodami `dodaj()`, `odejmij()`,
`pomnóż()`, i `podziel()`, które wykonują podstawowe operacje arytmetyczne."""

class Kalkulator:
    @staticmethod
    def dodaj(a, b):
        print(f"Suma =  {a+b}")

    @staticmethod
    def odejmij(a, b):
        print(f"Różnica =  {a-b}")

    @staticmethod
    def pomnoz(a, b):
        print(f"Iloczyn =  {a*b}")
        
    @staticmethod
    def podziel(a, b):
        if b != 0:
            print(f"Iloraz =  {a/b}")
        else:
            print("B jest zerem!!!")

kalkulator = Kalkulator()
kalkulator.dodaj(4, 5)
kalkulator.odejmij(43, 5)
kalkulator.pomnoz(7, 5)
kalkulator.podziel(4, 2)

print("\n-----------------------------------------------------------------------------\n")
"""19. Klasa `Telefon`: Napisz klasę `Telefon` z atrybutami `marka`, `model`,
`numer_telefonu`, oraz metodą `rozmowa_telefoniczna()`, która symuluje rozmowę
telefoniczną."""

class Telefon:
    def __init__(self, marka, model, numer_telefonu):
        self.marka = marka
        self.model = model
        self.numer_telefonu = numer_telefonu

    def rozmowa_telefoniczna(self):
        print(f"Rozmowa telefoniczna z {self.numer_telefonu}, wykonywana jest z {self.marka} {self.model}")

telefon = Telefon("Samsung", "S25 Ultra", "666999000")
telefon.rozmowa_telefoniczna()

print("\n-----------------------------------------------------------------------------\n")
"""20. Klasa `Kalendarz`: Zbuduj klasę `Kalendarz` z metodą `dodaj_wydarzenie` do
dodawania nowego wydarzenia i `wyświetl_wydarzenia()` do wyświetlania zapisanych
wydarzeń."""

class Kalendarz:
    def __init__(self):
        self.wydarzenia = []

    def dodaj_wydarzenie(self, data, wydarzenia):
        self.wydarzenia.append((data, wydarzenia))

    def wyswietl_wydarzenia(self):
        print("Wydarzenia w kalendarzu:")
        for data, wydarzenia in self.wydarzenia:
            print(f"{data} - {wydarzenia}")

kalendarz = Kalendarz()
kalendarz.dodaj_wydarzenie(6.05, "Serwis ASO")
kalendarz.dodaj_wydarzenie(24.05, "Wizyta u doktora")
kalendarz.wyswietl_wydarzenia()







