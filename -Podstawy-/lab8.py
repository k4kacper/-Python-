# # Zadanie 2
#
# slownik = {'d1' : 1.1, 'd2' : 2.2, 'd3' : 3.3}
# wynik = 1
# for i in slownik.values():
#     wynik *= i
#
# print("Wynik wynosi ", round(wynik, 3))

# # Zadanie 3
#
# slownik1 = {'d1' : 1.1, 'd2' : 2.2, 'd3' : 3.3}
# slownik2 = {'d4' : 4.4, 'd5' : 5.5, 'd6' : 6.6}
#
# slownik1.update(slownik2)
# print("Słownik1 po aktualizacji ", slownik1)

# # Zadanie 4
# slownik = {}
# n = int(input("Podaj ilość elementów w słowniku: "))
# for i in range(1,n+1):
#     slownik.update({i:i**3})
#
# print(slownik)

# # Zadanie 5
# slownik = {'a': 'A201', 'd': 'B202', 'c':'B202', 'b':'H018', 'f':'H018', 'e': 'A007', 'g': 'G230'}
# klucze = list(slownik.keys())
# klucze.sort()
#
# slownik_sort = {i: slownik[i] for i in klucze}
# print(slownik_sort)

# # Zadanie 6
# slownik = {'a': 'A201', 'b': 'B202', 'c':'B202', 'd':'H018', 'e':'H018', 'f': 'A007', 'g': 'G230'}
# print(set(slownik.values()))

# # Zadanie 7
# slownik = {}
#
# slowo = input("Podaj wyraz: ")
# for i in range(len(slowo)):
#     slownik[i+1] = slowo[i]
#
# print(slownik)
# 
# # Zadanie 8
# slownik = {'a': 'A201', 'b': 'B202', 'c': 'B202'}
# print(slownik)
# klucz = input('Wprowadź klucz: ')
# wartosc = input('Wprowadź wartość: ')
# wystapienia = 0
#
# for k, w in slownik.items():
#     if k == klucz and w == wartosc:
#         wystapienia += 1
#
# print("Częstość występowania pary klucz:wartość",klucz, ":", wartosc, "wynosi:", wystapienia)


