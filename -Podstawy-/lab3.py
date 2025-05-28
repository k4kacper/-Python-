# Zadanie 2
print("|Pętla for|")
for i in range(1,11):
    print(i, end=" ")
i = 1
print("")
print("|Pętla while|")
while i <= 10:
    print(i, end=" ")
    i += 1

# Zadanie 3
print("")
x = int(input("Podaj ilość liczb w silnii: "))
silnia = 1
for i in range(1, x+1, 1):
    silnia *= i
print("Silnia z ", x, "wynosi: ", silnia)

# Zadanie 4
for i in range(1, 21):
    if i % 2 == 0:
        print("Liczba parzysta: ", i)

# Zadanie 5
i = 1
while i <= 30:
    if i % 3 == 0:
        print("Liczba podzielna przez 3: ",i)
    i += 1

# Zadanie 6
for i in range(1, 31):
    if i % 2 == 0:
        print("Liczba parzysta: ", i)
    else:
        continue

# Zadanie 7
def alfabet(x):
    obecna_litera = 'a'
    while obecna_litera <= x:
        print(obecna_litera, end=' ')
        obecna_litera = chr(ord(obecna_litera) + 1)
alfabet(input("Podaj literę kończącą: "))
print("")

# Zadanie 8
x = int(input("Podaj liczbę: "))
suma = 0
i = 1
while i <= x:
    suma += i
    i += 1
print("Suma liczb wynosi: ", suma)

# Zadanie 9
def parzyste(x):
    suma = 0
    for i in range(x):
        if i % 2 == 0:
            suma += i
    print("Suma liczb parzystych wynosi: ", suma)

liczba = int(input("Podaj liczbe: "))
parzyste(liczba)

# Zadanie 10
print("|Pętla for|")
for i in range(100, 0, -1):
    if i % 2 != 0:
        if i % 3 == 0:
            print("Liczba podzielna przez 3 lecz nie przez 2: ", i)
print("|Pętla while|")
i = 100
while i >= 0:
    if i % 2 != 0:
        if i % 3 == 0:
            print("Liczba podzielna przez 3 lecz nie przez 2: ", i)
    i -= 1

# Zadanie 11
for i in range(100, -101, -1):
    if i % 8 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 2 == 0:
        print("Liczby podzielna przez 2 ale nie przez 3 i 8: ", i)

# Zadanie 12
import random
for i in range(8):
    for j in range(8):
        print(random.randint(0,1), end=" ")
    print("")

# Zadanie 13
for i in range(1,6):
    for j in range(1,6):
        print(i*j, end=" ")
    print("")