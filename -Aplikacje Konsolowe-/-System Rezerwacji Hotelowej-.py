"""System Rezerwacji Hotelowej:
Utwórz aplikację do zarządzania rezerwacjami hotelowymi z klasami Hotel, Pokój, Rezerwacja. Aplikacja powinna umożliwiać dodawanie pokoi do hotelu, tworzenie rezerwacji oraz wyświetlanie dostępnych pokoi."""

class Pokoj:
    def __init__(self, numer, typ, cena, dostepny=True):
        self.numer = numer
        self.typ = typ
        self.cena = cena
        self.dostepny = dostepny

    def __str__(self):
        status = "Dostępny" if self.dostepny else "Zajęty"
        return f"Pokój {self.numer} ({self.typ}), Cena: {self.cena} zł, Status: {status}"

class Hotel:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.pokoje = []

    def dodaj_pokoj(self, numer, typ, cena):
        self.pokoje.append(Pokoj(numer, typ, cena))

    def wyswietl_dostepne_pokoje(self):
        print(f"\nDostępne pokoje w hotelu {self.nazwa}:")
        for pokoj in self.pokoje:
            if pokoj.dostepny:
                print(pokoj)

class Rezerwacja:
    def __init__(self, hotel, numer_pokoju, klient):
        self.hotel = hotel
        self.numer_pokoju = numer_pokoju
        self.klient = klient
        self.zarezerwuj_pokoj()

    def zarezerwuj_pokoj(self):
        for pokoj in self.hotel.pokoje:
            if pokoj.numer == self.numer_pokoju and pokoj.dostepny:
                pokoj.dostepny = False
                print(f"\nRezerwacja zakończona sukcesem! Pokój {pokoj.numer} dla {self.klient}.")
                return
        print("\nPokój niedostępny lub nie istnieje.")

def main():
    hotel = Hotel("Hotel Wrocław")

    while True:
        print("\n1. Dodaj pokój")
        print("2. Wyświetl dostępne pokoje")
        print("3. Zarezerwuj pokój")
        print("4. Zakończ")

        wybor = input("\nWybierz opcję: ")

        if wybor == "1":
            numer = int(input("Numer pokoju: "))
            typ = input("Typ pokoju: ")
            cena = float(input("Cena za noc: "))
            hotel.dodaj_pokoj(numer, typ, cena)
            print("Pokój dodany!")

        elif wybor == "2":
            hotel.wyswietl_dostepne_pokoje()

        elif wybor == "3":
            klient = input("Podaj imię i nazwisko rezerwującego: ")
            numer_pokoju = int(input("Numer pokoju do rezerwacji: "))
            Rezerwacja(hotel, numer_pokoju, klient)

        elif wybor == "4":
            print("Zakończono działanie programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()
