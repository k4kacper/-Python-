import math
# # Zadanie 1
# h = int(input("Podaj wysokość walca:"))
# r = int(input("Podaj promień walca:"))
#
# V = math.pi * r**2 * h
# S = (2 * math.pi * r**2) + (2 * math.pi * r * h)
#
# print("Objętość walca wynosi: ", V)
# print("Powierzchnia walca wynosi: ", S)

# # Zadanie 2
# liczba = int(input("Podaj liczbę: "))
#
# suma = 1
# for i in range(2, int(math.sqrt(liczba)) + 1):
#     if liczba % i == 0:
#         suma += i
#         if i != liczba // i:
#             suma += liczba // i
#
# if suma > liczba:
#     print("Liczba", liczba," jest obfita.")
# else:
#     print("Liczba", liczba," nie jest obfita.")

# # Zadanie 3
# v = int(input("Podaj prędkość wiatru: "))
# T = int(input("Podaj temerature: "))
#
# To = 13.12 + 0.6215 * T - 11.37 * (v ** 0.16) + 0.3965 * T * (v ** 0.16)
#
# print("Temperatura odczuwalna wynosi:", round(To, 2))

# # Zadanie 4
# poczatkowa_szer = float(input("Podaj początkową szerokość: "))
# poczatkowa_dlug = float(input("Podaj początkową długość: "))
# koncowa_szer = float(input("Podaj końcową szerokość: "))
# koncowa_dlug = float(input("Podaj końcową długość: "))
#
# R = 6371
#
# poczatkowa_szer = math.radians(poczatkowa_szer)
# poczatkowa_dlug = math.radians(poczatkowa_dlug)
# koncowa_szer = math.radians(koncowa_szer)
# koncowa_dlug = math.radians(koncowa_dlug)
#
# delta_szer = koncowa_szer - poczatkowa_szer
# delta_dlug = koncowa_dlug - poczatkowa_dlug
#
# a = math.sin(delta_szer / 2) ** 2 + math.cos(poczatkowa_szer) * math.cos(koncowa_szer) * math.sin(delta_dlug / 2) ** 2
# c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#
# odleglosc = R * c
#
# print("Odległosć między punktami wynosi: ", round(odleglosc, 2), "km")

# # Zadanie 5
# real1 = float(input("Podaj część rzeczywistą pierwszej liczby zespolonej: "))
# imag1 = float(input("Podaj część urojoną pierwszej liczby zespolonej: "))
# real2 = float(input("Podaj część rzeczywistą drugiej liczby zespolonej: "))
# imag2 = float(input("Podaj część urojoną drugiej liczby zespolonej: "))
#
# z1 = complex(real1, imag1)
# z2 = complex(real2, imag2)
#
# suma, roznica, iloczyn, iloraz = 0, 0, 0, 0
# suma = z1 + z2
# roznica = z1 - z2
# iloczyn = z1 * z2
# if z2 != 0:
#     iloraz = z1 / z2
# else:
#     print("Nie można dzielić przez 0!")
#
# print("Suma wynosi: ", suma)
# print("Różnica wynosi: ", roznica)
# print("Iloczyn wynosi: ", iloczyn)
# print("Iloraz wynosi: ", iloraz)

# # Zadanie 6
# liczby = input("Podaj liczby oddzielone spacjami: ").split()
# liczby = [float(x) for x in liczby]
# srednia = sum(liczby) / len(liczby)
# suma_kwadratow = sum((x - srednia) ** 2 for x in liczby)
# odchylenie_standardowe = math.sqrt(suma_kwadratow / len(liczby))
# print("Odchylenie standardowe wynosi:", round(odchylenie_standardowe, 2))

