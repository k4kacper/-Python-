"""Aplikacja Zarządzania Kontaktami:
Utwórz aplikację do zarządzania książką adresową z klasami Kontakt, Grupa. Aplikacja powinna umożliwiać dodawanie kontaktów do grup, wyszukiwanie kontaktów oraz wyświetlanie listy kontaktów w grupie."""

class Kontakt:
    def __init__(self, imie, nazwisko, numer):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Tel: {self.numer}"

class Grupa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.kontakty = []

    def dodaj_kontakt(self, kontakt):
        self.kontakty.append(kontakt)

    def wyszukaj_kontakt(self, imie_nazwisko):
        for kontakt in self.kontakty:
            if f"{kontakt.imie} {kontakt.nazwisko}" == imie_nazwisko:
                return kontakt
        return None

    def wyswietl_kontakty(self):
        print(f"\nKontakty w grupie '{self.nazwa}':")
        for kontakt in self.kontakty:
            print(f"- {kontakt}")

def main():
    grupy = {}

    while True:
        print("\n1. Dodaj grupę")
        print("2. Dodaj kontakt do grupy")
        print("3. Wyszukaj kontakt")
        print("4. Wyświetl kontakty w grupie")
        print("5. Zakończ")

        wybor = input("\nWybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę grupy: ")
            if nazwa not in grupy:
                grupy[nazwa] = Grupa(nazwa)
                print(f"Dodano grupę: {nazwa}")
            else:
                print("Grupa już istnieje.")

        elif wybor == "2":
            nazwa = input("Podaj nazwę grupy: ")
            if nazwa in grupy:
                imie = input("Podaj imię kontaktu: ")
                nazwisko = input("Podaj nazwisko kontaktu: ")
                numer = input("Podaj numer telefonu: ")
                kontakt = Kontakt(imie, nazwisko, numer)
                grupy[nazwa].dodaj_kontakt(kontakt)
                print(f"Dodano kontakt '{imie} {nazwisko}' do grupy '{nazwa}'.")
            else:
                print("Grupa nie istnieje. Dodaj ją najpierw.")

        elif wybor == "3":
            nazwa = input("Podaj nazwę grupy: ")
            if nazwa in grupy:
                imie_nazwisko = input("Podaj imię i nazwisko kontaktu: ")
                kontakt = grupy[nazwa].wyszukaj_kontakt(imie_nazwisko)
                if kontakt:
                    print(f"\nZnaleziono kontakt: {kontakt}")
                else:
                    print("Kontakt nie istnieje.")
            else:
                print("Grupa nie istnieje.")

        elif wybor == "4":
            nazwa = input("Podaj nazwę grupy: ")
            if nazwa in grupy:
                grupy[nazwa].wyswietl_kontakty()
            else:
                print("Grupa nie istnieje.")

        elif wybor == "5":
            print("Zakończono działanie programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()