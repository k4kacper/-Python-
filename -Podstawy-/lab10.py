# # Zadanie 2
# nazwa_pliku = 'plik.txt'
# with open(nazwa_pliku, 'r') as plik:
#     linie = plik.readlines()
# dane = [linia.strip() for linia in linie]
#
# print(dane)

# # Zadanie 3
# plik_wejsciowy = 'plik.txt'
# plik_wyjsciowy = 'plik1.txt'
#
# with open(plik_wejsciowy, 'r') as w:
#     zawartosc = w.read()
# with open(plik_wyjsciowy, 'w') as z:
#     z.write(zawartosc)

# # Zadanie 4
# plik = 'plik.txt'
#
# with open(plik, 'r') as f:
#     zawartosc = f.read()
#
# slowa = zawartosc.split()
#
# najdluzsze_slowa = sorted(set(slowa), key=len, reverse=True)
# print(najdluzsze_slowa[0])

# # Zadanie 5
# from collections import Counter
# plik = 'plik.txt'
#
# with open(plik, 'r') as f:
#     zawartosc = f.read().lower()
#
# slowa = zawartosc.split()
# licznik = Counter(slowa)
# print(licznik)

# # Zadanie 6
# import random
# plik = 'plik.txt'
#
# with open(plik, 'r') as f:
#     zawartosc = f.read()
#
# slowa = zawartosc.split()
# losowe_slowa = random.sample(slowa, min(10, len(slowa)))
# print(losowe_slowa)

# # Zadanie 7
# plik = 'plik.txt'
# n = 5
#
# with open(plik, 'r') as f:
#     linie = f.readlines()
# n = int(input("Podaj ilość linii do wyświetlenia: "))
# ostatnie_n_linie = linie[-n:]
# print(ostatnie_n_linie)

# # Zadanie 8
# plik1 = 'plik1.txt'
# plik2 = 'plik2.txt'
# plik_wynikowy = 'plik_wynikowy.txt'
#
# with open(plik1, 'r') as f1:
#     linie1 = f1.readlines()
#
# with open(plik2, 'r') as f2:
#     linie2 = f2.readlines()
#
# with open(plik_wynikowy, 'w') as f_wynikowy:
#     for l1, l2 in zip(linie1, linie2):
#         f_wynikowy.write(l1.strip() + ' ' + l2.strip() + '\n')

# # Zadanie 9
# plik = 'plik_s.txt'
#
# with open(plik, 'r') as f:
#     zawartosc = f.read()
#
# zawartosc_bez_spacji = zawartosc.replace(' ', '')
#
# with open(plik, 'w') as f:
#     f.write(zawartosc_bez_spacji)
