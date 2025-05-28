"""Prosty System Zarządzania Szkołą:
Utwórz system zarządzania szkołą z klasami takimi jak Szkoła, Nauczyciel, Uczeń i Przedmiot. System powinien umożliwiać dodawanie nauczycieli i uczniów do przedmiotów oraz wyświetlanie listy uczniów zapisanych na dany przedmiot."""

class Uczen:
    def __init__(self, imie):
        self.imie = imie

class Nauczyciel:
    def __init__(self, imie):
        self.imie = imie

class Przedmiot:
    def __init__(self, nazwa, nauczyciel):
        self.nazwa = nazwa
        self.nauczyciel = nauczyciel
        self.uczniowie = []

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)

    def pokaz_uczniow(self):
        lista_uczniow = ", ".join(uczen.imie for uczen in self.uczniowie)
        return f"Przedmiot: {self.nazwa}, Nauczyciel: {self.nauczyciel.imie}, Uczniowie: {lista_uczniow if lista_uczniow else 'Brak zapisanych uczniow'}"

class Szkola:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.nauczyciele = []
        self.uczniowie = []
        self.przedmioty = []

    def dodaj_nauczyciela(self, nauczyciel):
        self.nauczyciele.append(nauczyciel)

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        return "\n".join(przedmiot.pokaz_uczniow() for przedmiot in self.przedmioty)

def menu():
    szkola = Szkola("Technikum nr.2")

    while True:
        print("\nWybierz opcje:")
        print("1. Dodaj nauczyciela")
        print("2. Dodaj ucznia")
        print("3. Dodaj przedmiot")
        print("4. Przypisz ucznia do przedmiotu")
        print("5. Wyswietl przedmioty")
        print("6. Wyjdz")

        wybor = input("\nTwoj wybor: ")

        if wybor == "1":
            imie = input("Podaj imie nauczyciela: ")
            szkola.dodaj_nauczyciela(Nauczyciel(imie))

        elif wybor == "2":
            imie = input("Podaj imie ucznia: ")
            szkola.dodaj_ucznia(Uczen(imie))

        elif wybor == "3":
            nazwa_przedmiotu = input("Podaj nazwe przedmiotu: ")
            if not szkola.nauczyciele:
                print("Brak nauczycieli w szkole. Dodaj nauczyciela najpierw.")
            else:
                print("\nLista nauczycieli:")
                for i, nauczyciel in enumerate(szkola.nauczyciele):
                    print(f"{i+1}. {nauczyciel.imie}")
                indeks = int(input("Wybierz numer nauczyciela: ")) - 1
                if 0 <= indeks < len(szkola.nauczyciele):
                    nauczyciel = szkola.nauczyciele[indeks]
                    szkola.dodaj_przedmiot(Przedmiot(nazwa_przedmiotu, nauczyciel))
                else:
                    print("Nieprawidlowy numer nauczyciela.")

        elif wybor == "4":
            if not szkola.uczniowie or not szkola.przedmioty:
                print("Brak uczniow lub przedmiotow w szkole.")
            else:
                print("\nLista uczniow:")
                for i, uczen in enumerate(szkola.uczniowie):
                    print(f"{i+1}. {uczen.imie}")
                indeks_ucznia = int(input("Wybierz numer ucznia: ")) - 1

                print("\nLista przedmiotow:")
                for i, przedmiot in enumerate(szkola.przedmioty):
                    print(f"{i+1}. {przedmiot.nazwa} - {przedmiot.nauczyciel.imie}")
                indeks_przedmiotu = int(input("Wybierz numer przedmiotu: ")) - 1

                if 0 <= indeks_ucznia < len(szkola.uczniowie) and 0 <= indeks_przedmiotu < len(szkola.przedmioty):
                    szkola.przedmioty[indeks_przedmiotu].dodaj_ucznia(szkola.uczniowie[indeks_ucznia])
                else:
                    print("Nieprawidlowy wybor.")

        elif wybor == "5":
            print("\nPrzedmioty w szkole:")
            print(szkola.pokaz_przedmioty())

        elif wybor == "6":
            print("Zakonczono program.")
            break

        else:
            print("Niepoprawna opcja, sproboj ponownie.")

menu()