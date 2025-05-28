# zadanie 1
x = 42
y = 12
print("Reszta z dzielenia wynosi: ", x % y)

# zadanie 2
x = 43
y = 12
print("Wynik dzielenia bez reszty wynosi: ", x / y)

# zadanie 3
nazwa = input("Podaj nazwę książki: ")
rok = input("Podaj rok wydania książki: ")
cena = float(input("Podaj cenę książki: "))
print("Książka nazywa się ", nazwa, " została wydana w ", rok, ", kosztuje ", cena, " zł")

# zadanie 4
liczba1 = float(input("Podaj liczbę ujemną rzeczywistą: "))
liczba2 = float(input("Podaj liczbę dodatnią rzeczywistą: "))
liczba1 = liczba1**2
liczba2 = liczba2**2
print("Pierwsza liczba wynosi: ", liczba1, " Druga liczba wynosi: ", liczba2)

# zadanie 5
import math
promien = int(input("Podaj promień koła: "))
wysokosc = int(input("Podaj wysokość: "))
objetosc =  1/3 * (wysokosc * math.pi * promien**2)
pole_p = math.pi * promien**2
l = wysokosc**2 + promien**2
l = math.sqrt(l)
pole_b = math.pi * promien * l
pole_c = pole_p + pole_b
print("Objętość stożka wynosi: %.2f" % objetosc)
print("Pole stożka wynosi: %.2f" % pole_c)

# zadanie 6
liczba = int(input("Podaj liczbę całkowitą: "))
if liczba % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

# zadanie 7
wyraz = int(input("Podaj pierwszy wyraz ciągu arytmetycznego: "))
roznica = int(input("Podaj różnicę ciągu arytmetycznego: "))
n = int(input("Podaj ilość wyrazów: "))

for i in range(n):
    print(wyraz)
    wyraz += roznica
    i = i + 1

# zadanie 8
wyraz = int(input("Podaj pierwszy wyraz ciągu geometrycznego: "))
roznica = int(input("Podaj różnicę ciągu geometrycznego: "))
n = int(input("Podaj ilość wyrazów: "))

for i in range(n):
    print(wyraz)
    wyraz *= roznica
    i = i + 1
