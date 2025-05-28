"""System Wypożyczalni Filmów:
Utwórz aplikację do zarządzania wypożyczalnią filmów z klasami Film, Klient, Wypożyczenie. Aplikacja powinna umożliwiać dodawanie filmów, rejestrowanie wypożyczeń oraz wyświetlanie historii wypożyczeń klienta."""

class Film:
    def __init__(self, tytul, rok, dostepny=True):
        self.tytul = tytul
        self.rok = rok
        self.dostepny = dostepny

    def __str__(self):
        status = "Dostępny" if self.dostepny else "Wypożyczony"
        return f"{self.tytul} ({self.rok}) - {status}"


class Klient:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.historia_wypozyczen = []

    def wypozycz_film(self, film):
        if film.dostepny:
            film.dostepny = False
            self.historia_wypozyczen.append(film)
            print(f"\n{self.imie} {self.nazwisko} wypożyczył/a '{film.tytul}'.")
        else:
            print("\nFilm jest niedostępny.")

    def wyswietl_historia(self):
        print(f"\nHistoria wypożyczeń - {self.imie} {self.nazwisko}:")
        if self.historia_wypozyczen:
            for film in self.historia_wypozyczen:
                print(f"- {film.tytul} ({film.rok})")
        else:
            print("Brak wypożyczonych filmów.")


class Wypozyczalnia:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.filmy = []
        self.klienci = {}

    def dodaj_film(self, tytul, rok):
        self.filmy.append(Film(tytul, rok))

    def dodaj_klienta(self, imie, nazwisko):
        self.klienci[f"{imie} {nazwisko}"] = Klient(imie, nazwisko)

    def wyswietl_filmy(self):
        print(f"\nFilmy w wypożyczalni '{self.nazwa}':")
        for film in self.filmy:
            print(f"- {film}")

    def wypozycz_film(self, imie_nazwisko, tytul_filmu):
        klient = self.klienci.get(imie_nazwisko)
        film = next((f for f in self.filmy if f.tytul == tytul_filmu), None)

        if klient and film:
            klient.wypozycz_film(film)
        else:
            print("\nNie znaleziono klienta lub filmu.")


def main():
    wypozyczalnia = Wypozyczalnia("FilmMax")

    while True:
        print("\n1. Dodaj film")
        print("2. Dodaj klienta")
        print("3. Wyświetl dostępne filmy")
        print("4. Wypożycz film")
        print("5. Wyświetl historię wypożyczeń klienta")
        print("6. Zakończ")

        wybor = input("\nWybierz opcję: ")

        if wybor == "1":
            tytul = input("Podaj tytuł filmu: ")
            rok = input("Podaj rok produkcji: ")
            wypozyczalnia.dodaj_film(tytul, rok)
            print("Film dodany!")

        elif wybor == "2":
            imie = input("Podaj imię klienta: ")
            nazwisko = input("Podaj nazwisko klienta: ")
            wypozyczalnia.dodaj_klienta(imie, nazwisko)
            print(f"Dodano klienta {imie} {nazwisko}.")

        elif wybor == "3":
            wypozyczalnia.wyswietl_filmy()

        elif wybor == "4":
            imie_nazwisko = input("Podaj imię i nazwisko klienta: ")
            tytul_filmu = input("Podaj tytuł filmu do wypożyczenia: ")
            wypozyczalnia.wypozycz_film(imie_nazwisko, tytul_filmu)

        elif wybor == "5":
            imie_nazwisko = input("Podaj imię i nazwisko klienta: ")
            klient = wypozyczalnia.klienci.get(imie_nazwisko)
            if klient:
                klient.wyswietl_historia()
            else:
                print("Klient nie istnieje.")

        elif wybor == "6":
            print("Zakończono działanie programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()