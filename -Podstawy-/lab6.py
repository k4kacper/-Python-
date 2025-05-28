import numpy as np

# # Zadanie 2
# tab1 = [1.1, 2.2, 3.3]
# tab2 = [4.4, 5.5, 6.6]
# wynik = []
#
# i = 0
# while i < len(tab1):
#     wynik.append(tab1[i])
#     i += 1
#
# i = 0
# while i < len(tab2):
#     wynik.append(tab2[i])
#     i += 1
#
# print("Końcowa tablica: ", wynik)

# # Zadanie 3
# tab = [1, 2, 3, 4, 5, 6, 3, 8, 9, 10]
# def zlicz(x):
#     i = 0
#     licz = 0
#     pierwsze = -1
#     while i < len(tab):
#         if tab[i] == x:
#             licz += 1
#             if pierwsze == -1:
#                 pierwsze = i
#         i += 1
#     print("Liczba została znaleziona",licz)
#     print("Pierwsze wystąpienie liczby",pierwsze)
# print(tab)
# zlicz(int(input("Podaj które liczbe chcesz policzyć: ")))

# Zadanie 4
# tab = []
# for i in range(20, 0, -1):
#     tab.append(i)
# print(tab)
# i = 0
# while i < len(tab):
#     if tab[i] % 3 == 0 or tab[i] % 7 == 0:
#         tab.pop(i)
#         i += 1
#     else:
#         i += 1
# print(tab)

# # Zadanie 5
# tab = []
# n = int(input("Podaj ilość liczb do wprowadzenia: "))
# for i in range(0, n):
#     tab.append(int(input("Podaj liczbe do tablicy: ")))
# print(tab)
# suma = 0
# srednia = 0
# for i in range(0, n):
#     suma += tab[i]
#
# srednia = suma / n
# print("Suma wynosi: ", suma)
# print("Średnia wynosi: ", srednia)

# # Zadanie 6
# tab = []
# for i in range(0, 4):
#    tab.append(float(input("Podaj liczbe do tablicy: ")))
# print(tab)
# min = tab[0]
# max = tab[0]
# for i in range(len(tab)):
#     if tab[i] <= min:
#         min = tab[i]
#     if tab[i] >= max:
#         max = tab[i]
#
# print("Maksimum wynosi: ", max)
# print("Minimum wynosi: ", min)

# # Zadanie 7
# import random
# tab = []
# for i in range(0, 5):
#     tab.append(round(random.uniform(0, 20),2))
# print(tab)
#
# min = tab[0]
# max = tab[0]
# min_i = 0
# max_i = 0
# for i in range(len(tab)-1):
#     if tab[i] <= min:
#         min = tab[i]
#         min_i = i
#     if tab[i] >= max:
#         max = tab[i]
#         max_i = i
#
# tab.pop(min_i)
# tab.pop(max_i)
# print(tab)
#
# print("Suma not za styl wynosi:",sum(tab))

# # Zadanie 8
# def jodełka(n):
#     tablica = np.zeros((n, n), dtype=int)
#
#     for i in range(n):
#         for j in range(n):
#             if j <= i:
#                 tablica[i][j] = j + 1
#             else:
#                 tablica[i][j] = i + 1
#
#     for wiersz in tablica:
#         for element in wiersz:
#             print(element, end=" ")
#         print()
#
# n = int(input("Podaj rozmiar tablicy: "))
# jodełka(n)

# # Zadanie 9
# def iloczyn(wiersze, kolumny):
#     tablica = np.zeros((wiersze, kolumny), dtype=int)
#     for i in range(wiersze):
#         for j in range(kolumny):
#             tablica[i][j] = (i + 1) * (j + 1)
#
#     for wiersz in tablica:
#         for element in wiersz:
#             print(element, end=" ")
#         print()
#
# wiersze = int(input("Podaj ilość wierszy tablicy: "))
# kolumny = int(input("Podaj ilość kolumn tablicy: "))
# iloczyn(wiersze, kolumny)