"""Prosta Gra w RPG:
Zaprojektuj prostą grę RPG z klasami, takimi jak Postać, Przeciwnik, Przedmiot. Gra powinna umożliwiać tworzenie postaci, walkę z przeciwnikami oraz zbieranie przedmiotów zwiększających statystyki postaci."""

import random


class Postac:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa
        self.poziom = 1
        self.doswiadczenie = 0
        self.ekwipunek = []

        # Statystyki według klasy
        if klasa == "Wojownik":
            self.sila = 15
            self.zdrowie = 120
            self.mana = 10
        elif klasa == "Mag":
            self.sila = 8
            self.zdrowie = 80
            self.mana = 40
        elif klasa == "Łucznik":
            self.sila = 12
            self.zdrowie = 100
            self.mana = 20
        else:
            raise ValueError("Niepoprawna klasa postaci!")

    def atakuj(self, przeciwnik):
        obrazenia = random.randint(1, self.sila)
        przeciwnik.zdrowie -= obrazenia
        print(f"{self.imie} atakuje {przeciwnik.imie} za {obrazenia} obrażeń!")

    def zdobadz_doswiadczenie(self, punkty):
        self.doswiadczenie += punkty
        if self.doswiadczenie >= self.poziom * 10:
            self.poziom += 1
            self.sila += 2
            self.zdrowie += 10
            self.mana += 5
            print(f"{self.imie} awansował na poziom {self.poziom}!")

    def zbierz_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)
        self.sila += przedmiot.bonus_sily
        self.zdrowie += przedmiot.bonus_zdrowia
        print(
            f"{self.imie} zdobył {przedmiot.nazwa}! (+{przedmiot.bonus_sily} siły, +{przedmiot.bonus_zdrowia} zdrowia)")


class Przeciwnik:
    def __init__(self, imie, sila, zdrowie):
        self.imie = imie
        self.sila = sila
        self.zdrowie = zdrowie

    def atakuj(self, postac):
        obrazenia = random.randint(1, self.sila)
        postac.zdrowie -= obrazenia
        print(f"{self.imie} atakuje {postac.imie} za {obrazenia} obrażeń!")


class Przedmiot:
    def __init__(self, nazwa, bonus_sily, bonus_zdrowia):
        self.nazwa = nazwa
        self.bonus_sily = bonus_sily
        self.bonus_zdrowia = bonus_zdrowia


imie = input("Podaj imię postaci: ")
klasa = input("Wybierz klasę postaci (Wojownik, Mag, Łucznik): ")
postac = Postac(imie, klasa)

przeciwnik = Przeciwnik("Ork", 10, 100)

miecz = Przedmiot("Miecz Mocy", 5, 10)
zbroja = Przedmiot("Zbroja Wojownika", 2, 20)

postac.zbierz_przedmiot(miecz)
postac.zbierz_przedmiot(zbroja)

while przeciwnik.zdrowie > 0 and postac.zdrowie > 0:
    postac.atakuj(przeciwnik)
    if przeciwnik.zdrowie > 0:
        przeciwnik.atakuj(postac)

if postac.zdrowie > 0:
    print(f"{postac.imie} wygrał walkę i zdobył doświadczenie!")
    postac.zdobadz_doswiadczenie(15)
else:
    print(f"{przeciwnik.imie} pokonał {postac.imie}!")
