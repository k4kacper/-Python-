import datetime

# # Zadanie 2
# dzisiaj = datetime.date.today()
# za_tydz = dzisiaj + datetime.timedelta(days=7)
#
# print("Dzisiaj jest: ", dzisiaj)
# print("Za tydzień będzie ", za_tydz)

# # Zadanie 3
# start_data = datetime.date(datetime.datetime.now().year, 1, 1)
# koniec_data = datetime.date(datetime.datetime.now().year, 2, 15)
#
# obecna_data = start_data
#
# while obecna_data.weekday() != 1:
#     obecna_data += datetime.timedelta(days=1)
#
# while obecna_data <= koniec_data:
#     print(obecna_data)
#     obecna_data += datetime.timedelta(weeks=1)

# # Zadanie 4
# biezacy_rok = datetime.datetime.now().year
#
# for i in range(1, 4):
#     rok = biezacy_rok + i
#     data_chrzest = datetime.date(rok, 1, 6)
#     while data_chrzest.weekday() != 6:
#         data_chrzest += datetime.timedelta(days=1)
#
#     print("Pierwsza niedziela po 6 stycznia", rok,":", data_chrzest)

# # Zadanie 5
# rok = datetime.datetime.now().year
# data_30_wrzesnia = datetime.date(rok, 9, 30)
# while data_30_wrzesnia.weekday() != 0:
#     data_30_wrzesnia += datetime.timedelta(days=1)
#
# print("Pierwszy poniedziałek po 30 września:", data_30_wrzesnia)

# # Zadanie 6
# dzisiaj = datetime.date.today()
# data_za_100_dni = dzisiaj + datetime.timedelta(days=100)
#
# print("Data za 100 dni:",data_za_100_dni)

# # Zadanie 7
# rok = datetime.datetime.now().year
# poczatek = datetime.date(rok, 3, 1)
# koniec = datetime.date(rok, 6, 30)
# soboty = []
# while poczatek.weekday() != 5:
#     poczatek += datetime.timedelta(days=1)
#
# while poczatek <= koniec:
#     soboty.append(poczatek)
#     poczatek += datetime.timedelta(weeks=1)
#
# print("Daty wszystkich sobót:")
# for sobota in soboty:
#     print(sobota)

# # Zadanie 8
# niedziele = []
# rok = datetime.datetime.now().year
# for miesiac in [1, 3, 5, 7, 9, 11]:
#     ostatni_dzien = datetime.date(rok, miesiac + 1, 1) - datetime.timedelta(days=1)
#     while ostatni_dzien.weekday() != 6:
#         ostatni_dzien -= datetime.timedelta(days=1)
#     niedziele.append(ostatni_dzien)
#
# print("Ostatnie niedziele w miesiącach nieparzystych:")
# for niedziela in niedziele:
#     print(niedziela)

# # Zadanie 9
# data_pocz = input("Podaj datę początkową (w formacie RRRR-MM-DD HH:MM:SS): ")
# data_pocz = datetime.datetime.strptime(data_pocz, "%Y-%m-%d %H:%M:%S")
#
# data_kon = input("Podaj datę końcową (w formacie RRRR-MM-DD HH:MM:SS): ")
# data_kon = datetime.datetime.strptime(data_kon, "%Y-%m-%d %H:%M:%S")
#
# roznica = (data_kon - data_pocz).total_seconds()
#
# print("Różnica w sekundach wynosi:", int(roznica), " sekund.")

# Zadanie 10
start_rok = 2023
end_rok = 2024
poniedzialki = []

for rok in range(start_rok, end_rok + 1):
    for miesiac in range(1, 13):
        pierwszy_dzien = datetime.date(rok, miesiac, 1)
        if pierwszy_dzien.weekday() == 0:
            poniedzialki.append(pierwszy_dzien)

print("Poniedziałki pierwszego dnia miesiąca:")
for poniedzialek in poniedzialki:
    print(poniedzialek)

