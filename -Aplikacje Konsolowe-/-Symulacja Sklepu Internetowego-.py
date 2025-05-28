"""Symulacja Sklepu Internetowego:
Stwórz aplikację symulującą sklep internetowy z klasami Produkt, Koszyk, Zamówienie. Aplikacja powinna umożliwiać dodawanie produktów do koszyka, składanie zamówień oraz wyświetlanie szczegółów zamówienia."""

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return f"{self.nazwa} - {self.cena} zł"

class Koszyk:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, produkt, ilosc=1):
        self.produkty.append((produkt, ilosc))

    def wyswietl_koszyk(self):
        print("\nProdukty w koszyku:")
        for produkt, ilosc in self.produkty:
            print(f"- {produkt.nazwa} ({produkt.cena} zł) x {ilosc}")

    def oblicz_sume(self):
        return sum(produkt.cena * ilosc for produkt, ilosc in self.produkty)

class Zamowienie:
    def __init__(self, koszyk, klient):
        self.koszyk = koszyk
        self.klient = klient
        self.suma = koszyk.oblicz_sume()

    def wyswietl_zamowienie(self):
        print(f"\nZamówienie dla {self.klient}:")
        self.koszyk.wyswietl_koszyk()
        print(f"Łączna kwota: {self.suma} zł")

def main():
    koszyk = Koszyk()

    while True:
        print("\n1. Dodaj produkt do koszyka")
        print("2. Wyświetl koszyk")
        print("3. Złóż zamówienie")
        print("4. Zakończ")

        wybor = input("\nWybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę produktu: ")
            cena = float(input("Podaj cenę produktu: "))
            ilosc = int(input("Podaj ilość: "))
            produkt = Produkt(nazwa, cena)
            koszyk.dodaj_produkt(produkt, ilosc)
            print("Produkt dodany do koszyka!")

        elif wybor == "2":
            koszyk.wyswietl_koszyk()

        elif wybor == "3":
            klient = input("Podaj imię i nazwisko zamawiającego: ")
            zamowienie = Zamowienie(koszyk, klient)
            zamowienie.wyswietl_zamowienie()

        elif wybor == "4":
            print("Zakończono działanie programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

main()