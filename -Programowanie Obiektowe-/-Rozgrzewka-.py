'Zadanie 1: Klasa i Obiekt'
'Opis: Zdefiniuj klasę `Samochod`, która ma atrybut `marka`. Utwórz obiekt tej klasy i przypisz markę "Toyota".'

class Samochod:
    def __init__(self, marka):
        self.marka = marka

samochod = Samochod("Toyota")

print('Marka samochodu: ', samochod.marka)

'Zadanie 2: Metoda Klasy'
'Opis: Napisz klasę `Kalkulator` z metodą `dodaj`, która przyjmuje dwie liczby jako argumenty i zwraca ich sumę.'

class Kalkulator:
    def dodaj(self,a,b):
        return a+b

kalkulator = Kalkulator()

print("Wynik dodawania:",kalkulator.dodaj(3,6))

'Zadanie 3: Konstruktory'
'Opis: Stwórz klasę `Osoba` z atrybutami `imie` i `wiek`, które są przypisywane przy tworzeniu obiektu.'

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

osoba = Osoba("Kacper", 20)
print(osoba.imie, osoba.wiek)

'Zadanie 4: Dziedziczenie'
'Opis:  Napisz klasę `Pojazd` z metodą `opis`. Utwórz klasę `Rower`, która dziedziczy po klasie `Pojazd` i nadpisuje metodę `opis`.'

class Pojazd:
    def opis(self):
        return "To jest pojazd"

class Rower(Pojazd):
    def opis(self):
        return "To jest rower"

rower = Rower()
print(rower.opis())

'Zadanie 5: Polimorfizm'
'Opis: Napisz dwie klasy `Kot` i `Pies`, każda z metodą `dzwiek`, która zwraca dźwięk charakterystyczny dla danego zwierzęcia.'


class Kot:
    def dzwiek(self):
        return "Miau"

class Pies:
    def dzwiek(self):
        return "Hau"

kot = Kot()
pies = Pies()
print(kot.dzwiek())
print(pies.dzwiek())

'Zadanie 6: Prywatne Atrybuty'
'Opis: Stwórz klasę `Bank` z prywatnym atrybutem `__saldo`. Dodaj metodę, która zwraca saldo.'

class Bank:
    def __init__(self, saldo):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo

bank = Bank(15000)
print(bank.get_saldo())

'Zadanie 7: Metoda Statyczna'
'Opis: Napisz klasę `Matematyka` z metodą statyczną `pi`, która zwraca wartość 3.14.'

class Matematyka:
    @staticmethod
    def pi():
        return 3.14

print(Matematyka.pi())

'Zadanie 8: Dekorator @ property'
'Opis: Utwórz klasę `Prostokat`z atrybutami `dlugosc` i `szerokosc`. Dodaj metodę z dekoratorem `@ property`, która zwraca pole powierzchni prostokąta.'

class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    @property
    def pole(self):
        return self.dlugosc * self.szerokosc

prostokat = Prostokat(5, 10)
print(prostokat.pole)

'Zadanie 9: Abstract Base Class'
'Opis: Napisz klasę abstrakcyjną `Ksztalt` z metodą `pole`. Utwórz klasę `Kwadrat`, która dziedziczy po `Ksztalt` i implementuje metodę `pole`.'

from abc import ABC, abstractmethod

class Ksztalt(ABC):
    @abstractmethod
    def pole(self):
        pass

class Kwadrat(Ksztalt):
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok * self.bok

kwadrat = Kwadrat(4)
print(kwadrat.pole())

'Zadanie 10: Kompozycja'
'Opis: Stwórz klasy `Silnik` i `Samochod`. Klasa `Samochod` powinna mieć atrybut `silnik` jako obiekt klasy `Silnik`.'

class Silnik:
    def __init__(self, moc):
        self.moc = moc

class Samochod:
    def __init__(self, marka, silnik):
        self.marka = marka
        self.silnik = silnik

silnik = Silnik(350)

samochod = Samochod("BMW", silnik)
print(samochod.silnik.moc)

'Zadanie 11: Dziedziczenie Wielokrotne'
'Opis: Napisz dwie klasy `A` i `B`, każda z metodą `opis`, a następnie klasę `C`, która dziedziczy po `A` i `B`, i wywołuje obie metody.'

class A:
    def opis(self):
        return "Klasa A"

class B:
    def opis(self):
        return "Klasa B"

class C(A, B):
    def opis(self):
        return super().opis() + " i " + B.opis(self)

c = C()
print(c.opis())

'Zadanie 12: Interfejsy'
'Opis: Stwórz interfejs `Pilot` z metodą `wlacz`. Utwórz klasę `Telewizor`, która implementuje interfejs `Pilot`.'

from abc import ABC, abstractmethod

class Pilot(ABC):
    @abstractmethod
    def wlacz(self):
        pass

class Telewizor(Pilot):
    def wlacz(self):
        return "Telewizor został włączony"

telewizor = Telewizor()
print(telewizor.wlacz())

'Zadanie 13: Klasy wewnętrzne'
'Opis: Napisz klasę `Komputer` z klasą wewnętrzną `Procesor`. Klasa `Procesor` powinna mieć metodę `specyfikacja`, która zwraca dane procesora.'

class Komputer:
    class Procesor:
        def __init__(self, model):
            self.model = model

        def specyfikacja(self):
            return f"Procesor: {self.model}"

procesor = Komputer.Procesor("Intel i9-9900K")
print(procesor.specyfikacja())

'Zadanie 14: Hermetyzacja'
'Opis: Utwórz klasę `KontoBankowe` z prywatnym atrybutem `__saldo` oraz metodami `wplata` i `wyplata` do zmiany salda.'

class KontoBankowe:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def wplata(self, kwota):
        self.__saldo += kwota

    def wyplata(self, kwota):
        if kwota <= self.__saldo:
            self.__saldo -= kwota
            return True
        return False

    def get_saldo(self):
        return self.__saldo

konto = KontoBankowe()
konto.wplata(14000)
konto.wyplata(5700)
print(konto.get_saldo())

'Zadanie 15: Operator Package Init'
'Opis: Utwórz pakiet `matematyka`, który zawiera funkcję `dodaj`. Zaimportuj ją i użyj w programie.'

from matematyka import dodaj

wynik = dodaj(5, 3)
print("Wynik dodawania: ", wynik)
