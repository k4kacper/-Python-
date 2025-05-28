# # Zadanie 2
# krotka1 = ('bialy', 'czerwony', 'zielony', 'niebieski', 'czarny')
# lista = list(krotka1)
# print("Podaj indeks elementu, który chcesz usunąć: ", len(lista), "- tyle jest elementów")
# n = int(input("Liczba: "))
# lista.pop(n-1)
# krotka2 = tuple(lista)
# print(krotka2)

# # Zadanie 3
# lista = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (3, 10, 11), (1, 2, 3)]
# print(lista)
# wartosc = int(input("Podaj szukaną wartość: "))
#
# indeksy = []
# for i, krotka in enumerate(lista):
#     if wartosc in krotka:
#         indeksy.append(i)
#
# print('Indeksy krotek zawierających wartość ', wartosc,':',indeksy)


# # Zadanie 4
# krotka = ('bialy', 'czerwony', 'zielony', 'niebieski', 'czarny')
# lista = list(krotka)
# lista_r = lista[::-1]
# krotka_r = tuple(lista_r)
# print(krotka_r)

# # Zadanie 5
# lista = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# nowa_lista = []
# for krotka in lista:
#     nowa_krotka = krotka[:-1] + (0,)
#     nowa_lista.append(nowa_krotka)
# print(nowa_lista)

# # Zadanie 6
# lista = [(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]
# nowa_lista = []
# nowa_lista = [krotka for krotka in lista if krotka]
# print(nowa_lista)

# # Zadanie 7
# krotka1 = ('bialy', 'czerwony', 'zielony', 'niebieski', 'czarny')
# lista = list(krotka1)
# lista.sort()
# krotka_sort = tuple(lista)
# print(krotka_sort)

# # Zadanie 8
# tekst = "Hello World!"
# krotka = tuple(tekst)
# print(krotka)

# # Zadanie 9
# krotki = ((1, 2, 3, 4), (10, 15, 25, 35), (70, 80, 90, 100), (-20, -15, -10, -5))
# liczba_krotek = len(krotki)
# srednie = []
#
# for i in range(len(krotki[0])):
#     suma = sum(krotka[i] for krotka in krotki)
#     srednia = suma / liczba_krotek
#     srednie.append(srednia)
#
# print(srednie)

# # Zadanie 10
# krotki = (('pon', 'wto', 'srd'), ('czw', 'ptk', 'sob'), ('ndz', 'pon', 'wto'))
# wartosc = input("Podaj wartosc którą sprawdzić: ")
# wynik = 0
# for krotka in krotki:
#         if wartosc in krotka:
#             wynik = True
#         else:
#             wynik = False
#
# print(wynik)


