"""Aplikacja Zarządzania Zadaniami (To-Do App):
Stwórz konsolową aplikację do zarządzania zadaniami z wykorzystaniem klas Zadanie, ListaZadan. Aplikacja powinna umożliwiać dodawanie, usuwanie i oznaczanie zadań jako ukończone oraz wyświetlanie listy zadań."""

class Zadanie:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.ukonczone = False

    def oznacz_ukonczone(self):
        self.ukonczone = True

class ListaZadan:
    def __init__(self):
        self.lista = []

    def dodaj_zadanie(self, zadanie):
        self.lista.append(zadanie)

    def usun_zadanie(self, indeks):
        if 0 <= indeks < len(self.lista):
            del self.lista[indeks]

    def pokaz_zadania(self):
        return [(zadanie.nazwa, zadanie.ukonczone) for zadanie in self.lista]

    def wyswietl_zadania(self):
        print("\n===== LISTA ZADAŃ =====")
        if not self.lista:
            print("Brak zadań na liście.")
        else:
            for indeks, (nazwa, ukonczone) in enumerate(self.pokaz_zadania(), start=1):
                status_txt = "[✓]" if ukonczone else "[ ]"
                print(f"{indeks}. {status_txt} {nazwa}")
        print("========================\n")

def menu():
    lista = ListaZadan()

    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Oznacz zadanie jako ukończone")
        print("4. Wyświetl listę zadań")
        print("5. Wyjdź")

        wybor = input("\nTwój wybór: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę zadania: ")
            lista.dodaj_zadanie(Zadanie(nazwa))
        elif wybor == "2":
            lista.wyswietl_zadania()
            indeks = int(input("Podaj numer zadania do usunięcia: ")) - 1
            lista.usun_zadanie(indeks)
        elif wybor == "3":
            lista.wyswietl_zadania()
            indeks = int(input("Podaj numer zadania do oznaczenia jako ukończone: ")) - 1
            if 0 <= indeks < len(lista.lista):
                lista.lista[indeks].oznacz_ukonczone()
        elif wybor == "4":
            lista.wyswietl_zadania()
        elif wybor == "5":
            print("Zakończenie programu.")
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

menu()