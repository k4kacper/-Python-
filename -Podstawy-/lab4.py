# Zadanie 2
def maks(a, b, c):
    if a > b and a > c:
        print("Max wynosi: ", a)
    elif b > a and b > c:
        print("Max wynosi: ", b)
    elif c > a and c > b:
        print("Max wynosi: ", c)
    else:
        print("Liczby są równe!")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

maks(a, b, c)

# Zadanie 3
def odwrot(znaki):
    print(znaki[::-1])

ciag = input("Podaj ciąg znaków do odwrócenia: ")
odwrot(ciag)

# Zadanie 4
def przedzial(liczba):
    if 0 <= liczba <= 100:
        print("Liczba jest w przedziale 0 - 100")
    else:
        print("Liczba jest poza przedziałem")

przedzial(int(input("Podaj liczbe: ")))

# Zadanie 5
def silnia(liczba):
    s = 1
    for i in range(1, liczba+1):
        s *= i
    print("Silnia wznosi: ", s)
ile = int(input("Podaj liczbe z której obliczyć silnie: "))
silnia(ile)

# Zadanie 6
def ilosc(ciag):
    duza = 0
    mala = 0
    for i in ciag:
        if i.isupper():
            duza += 1
        elif i.islower():
            mala += 1
    print("Ilość małych liter: ", mala, ", ilość dużych liter: ", duza)

ilosc(input("Podaj ciąg znaków: "))

# Zadanie 7
def doskonale(liczba):
    suma_d = 0
    for i in range(1, liczba // 2 + 1):
        if liczba % i == 0:
            suma_d += i
    if suma_d == liczba:
        print("Liczba", liczba, "jest doskonała!")
    else:
        print("Liczba", liczba, "nie jest doskonała!")

doskonale(int(input("Podaj liczbę: ")))

# Zadanie 8
def palindrom(wyraz):
    j = len(wyraz) - 1
    for i in range(len(wyraz) // 2):
        if wyraz[i] != wyraz[j]:
            print("Wyraz", wyraz, "nie jest palindromem")
            return
        j -= 1
    print("Wyraz", wyraz, "jest palindromem")


palindrom(input("Podaj wyraz: "))

# Zadanie 9
import random, math, time

def pierwiastek(x):
    time.sleep(1)
    print("Pierwiastek z", x, "wynosi:", math.sqrt(x))

pierwiastek(random.randint(1,1000))
