"""Konsolowy Kalendarz Wydarzeń:
Stwórz aplikację do zarządzania kalendarzem wydarzeń z klasami Wydarzenie, Kalendarz. Aplikacja powinna umożliwiać dodawanie, usuwanie i edytowanie wydarzeń """

class Wydarzenie:
    def __init__(self, nazwa, data, opis=""):
        self.nazwa = nazwa
        self.data = data
        self.opis = opis

    def __str__(self):
        return f"{self.data} - {self.nazwa}: {self.opis}"

class Kalendarz:
    def __init__(self):
        self.wydarzenia = []

    def dodaj_wydarzenie(self, nazwa, data, opis=""):
        self.wydarzenia.append(Wydarzenie(nazwa, data, opis))
        print("Dodano wydarzenie.")

    def usun_wydarzenie(self, nazwa):
        for wydarzenie in self.wydarzenia:
            if wydarzenie.nazwa == nazwa:
                self.wydarzenia.remove(wydarzenie)
                print("Usunięto wydarzenie.")
                return
        print("Nie znaleziono wydarzenia.")

    def edytuj_wydarzenie(self, nazwa, nowa_data=None, nowy_opis=None):
        for wydarzenie in self.wydarzenia:
            if wydarzenie.nazwa == nazwa:
                if nowa_data:
                    wydarzenie.data = nowa_data
                if nowy_opis:
                    wydarzenie.opis = nowy_opis
                print("Zaktualizowano wydarzenie.")
                return
        print("Nie znaleziono wydarzenia.")

    def wyswietl_wydarzenia(self):
        print("\nLista wydarzeń:")
        for wydarzenie in self.wydarzenia:
            print(f"- {wydarzenie}")

def main():
    kalendarz = Kalendarz()

    while True:
        print("\n1. Dodaj wydarzenie")
        print("2. Usuń wydarzenie")
        print("3. Edytuj wydarzenie")
        print("4. Wyświetl wszystkie wydarzenia")
        print("5. Zakończ")

        wybor = input("\nWybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę wydarzenia: ")
            data = input("Podaj datę wydarzenia: ")
            opis = input("Podaj opis wydarzenia (opcjonalnie): ")
            kalendarz.dodaj_wydarzenie(nazwa, data, opis)

        elif wybor == "2":
            nazwa = input("Podaj nazwę wydarzenia do usunięcia: ")
            kalendarz.usun_wydarzenie(nazwa)

        elif wybor == "3":
            nazwa = input("Podaj nazwę wydarzenia do edycji: ")
            nowa_data = input("Podaj nową datę (lub naciśnij Enter, aby pominąć): ")
            nowy_opis = input("Podaj nowy opis (lub naciśnij Enter, aby pominąć): ")
            kalendarz.edytuj_wydarzenie(nazwa, nowa_data if nowa_data else None, nowy_opis if nowy_opis else None)

        elif wybor == "4":
            kalendarz.wyswietl_wydarzenia()

        elif wybor == "5":
            print("Zakończono działanie programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()