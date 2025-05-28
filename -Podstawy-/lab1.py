# zdanie 1
print("Hello World!")

# zadanie 2
#Komentarz jednoliniowy
'''
Komentarz
Wieloliniowy
'''

# zadanie 3
liczba1 = 10
liczba2 = 3
liczba3 = 7
print("Dodawanie = ", liczba1+liczba2)
print("Odejmowanie = ", liczba1-liczba2)
print("Mnożenie = ", liczba1*liczba2)
print("Dzielenie = ", liczba1/liczba2)

# zadanie 4
a = 25
b = 23
c = 13
d = a % b % c
print("Wynik wynosi: ", d)

# zadanie 5
a = float(input("Podaj krótszy bok prostokąta: "))
b = float(input("Podaj dłuższy bok prostokąta: "))
pole = a * b
print("Pole prostokąta wynosi: %.2f" % pole)

# zadanie 6
import math
r = float(input("Podaj promień kuli: "))
powierzchnia = 4*(math.pi*r**2)
objetosc = 4/3*(math.pi*r**3)
print("Powierzchnia kuli = %.2f" % powierzchnia)
print("Objętość kuli = %.2f" % objetosc)

# zadanie 7
temperatura = int(input("Podaj temperature w stopniach Celsjusza: "))
print("Temperatura w Fahrenheitach wynosi: ", 32 + (9.0 * temperatura) / 5)

# zadanie 8
liczba = int(input("Podaj dowolną liczbę: "))
if liczba < 0:
    print("Liczba jest ujemna")
elif 0 <= liczba <= 100:
    print("Liczba jest w przedziale 0-100")
else:
    print("Liczba jest większa od 100")

# zadanie 9
while True:
    znak = input("Podaj dowolny znak: ")
    if znak == "c":
        print("Podałeś znak kończący pętle!")
        break
    else:
        input("Podaj dowolny znak: ")
