"""Biblioteka Muzyczna:
Stwórz aplikację do zarządzania biblioteką muzyczną z klasami Utwór, Album, Artysta. Aplikacja powinna umożliwiać dodawanie utworów do albumów, dodawanie albumów do artystów oraz wyświetlanie listy utworów danego artysty."""

class Utwor:
    def __init__(self, tytul, czas_trwania):
        self.tytul = tytul
        self.czas_trwania = czas_trwania

    def __str__(self):
        return f"{self.tytul} ({self.czas_trwania} min)"

class Album:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.utwory = []

    def dodaj_utwor(self, utwor):
        self.utwory.append(utwor)

    def wyswietl_utwory(self):
        print(f"\nAlbum: {self.nazwa}")
        for utwor in self.utwory:
            print(f"- {utwor}")

class Artysta:
    def __init__(self, imie):
        self.imie = imie
        self.albumy = []

    def dodaj_album(self, album):
        self.albumy.append(album)

    def wyswietl_utwory(self):
        print(f"\nArtysta: {self.imie}")
        for album in self.albumy:
            album.wyswietl_utwory()

def main():
    artysci = {}

    while True:
        print("\n1. Dodaj artystę")
        print("2. Dodaj album do artysty")
        print("3. Dodaj utwór do albumu")
        print("4. Wyświetl utwory artysty")
        print("5. Zakończ")

        wybor = input("\nWybierz opcję: ")

        if wybor == "1":
            imie = input("Podaj nazwę artysty: ")
            if imie not in artysci:
                artysci[imie] = Artysta(imie)
                print(f"Dodano artystę: {imie}")
            else:
                print("Artysta już istnieje.")

        elif wybor == "2":
            imie = input("Podaj nazwę artysty: ")
            if imie in artysci:
                album_nazwa = input("Podaj nazwę albumu: ")
                album = Album(album_nazwa)
                artysci[imie].dodaj_album(album)
                print(f"Dodano album '{album_nazwa}' do artysty {imie}.")
            else:
                print("Artysta nie istnieje. Dodaj go najpierw.")

        elif wybor == "3":
            imie = input("Podaj nazwę artysty: ")
            if imie in artysci:
                album_nazwa = input("Podaj nazwę albumu: ")
                album = next((a for a in artysci[imie].albumy if a.nazwa == album_nazwa), None)
                if album:
                    tytul = input("Podaj tytuł utworu: ")
                    czas_trwania = float(input("Podaj czas trwania utworu (min): "))
                    utwor = Utwor(tytul, czas_trwania)
                    album.dodaj_utwor(utwor)
                    print(f"Dodano utwór '{tytul}' do albumu '{album_nazwa}'.")
                else:
                    print("Album nie istnieje. Dodaj go najpierw.")
            else:
                print("Artysta nie istnieje. Dodaj go najpierw.")

        elif wybor == "4":
            imie = input("Podaj nazwę artysty: ")
            if imie in artysci:
                artysci[imie].wyswietl_utwory()
            else:
                print("Artysta nie istnieje.")

        elif wybor == "5":
            print("Zakończono działanie programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()