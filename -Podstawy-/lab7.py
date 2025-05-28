# # Zadanie 2
# lista = [1.1, 2.2, 3.3]
# wynik = 1
# for i in lista:
#     wynik *= i
# print("Wynik to: ", round(wynik, 3))
#
# # Zadanie 3
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min = lista[0]
# max = lista[0]
# for i in lista:
#     if min>i:
#         min = i
#     if max<i:
#         max = i
#
# print("Minimum w liście to: ", min)
# print("Maksimum w liście to: ", max)

# # Zadanie 4
# lista = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
#
# def usun_powtorzenia(lista):
#     wynik = []
#     for liczba in lista:
#         if liczba not in wynik:
#             wynik.append(liczba)
#     return wynik
#
# lista_bez_powtorzen = usun_powtorzenia(lista)
# print(lista_bez_powtorzen)

# # Zadanie 5
# znaki = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
# ciag = ''
# for i in znaki:
#     ciag += i
#
# print(ciag)

# # Zadanie 6
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [5, 6, 7, 8, 9, 10]
# wynik = []
#
# for i in lista1:
#     if i in lista2 and i not in wynik:
#         wynik.append(i)
#
# print("Jednakowe elementy: ", wynik)

# # Zadanie 7
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
# n = int(input("Podaj co ile elementów wypisywać: "))
#
# wynik = [lista[i::n] for i in range(n)]
# print(wynik)

# # Zadanie 8
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [5, 6, 7, 8, 9, 10]
#
# lista1.pop(-1)
# lista1.extend(lista2)
# print(lista1)

# # Zadanie 9
# lista = [1, 2, 3, 4, 5]
# slowo = "building"
# wynik = []
# for i in lista:
#     element = str(i)
#     wynik.append(slowo + element)
#
# print(wynik)

# # Zadanie 10
# lista = [3, 5, 0, 4, 0, 2, 11, 7, 0, 5, 9, 0]
# wynik = []
# liczba_zer = lista.count(0)
# for i in lista:
#     if i != 0:
#         wynik.append(i)
#
# wynik.extend([0] * liczba_zer)
# print(wynik)

# # Zadanie 11
# def sitoEratostenesa(n):
#     liczbyPierwsze = [True] * (n + 1)
#     liczbyPierwsze[0] = False
#     liczbyPierwsze[1] = False
#     for i in range(2, n + 1):
#         if liczbyPierwsze[i]:
#             j = i + i
#             while j <= n:
#                 liczbyPierwsze[j] = False
#                 j += i
#     return liczbyPierwsze
#
# n = int(input("Podaj wartość n: "))
# print("Liczby pierwsze od 0 do", n, ":")
# wynik = sitoEratostenesa(n)
#
# for i in range(2, n + 1):
#     if (wynik[i]):
#         print(i, end=" ")
