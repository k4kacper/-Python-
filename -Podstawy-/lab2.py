import math
# zadanie 2
liczba = int(input("Podaj liczbę całkowitą: "))
print("Wartość bezwzględna: ", abs(liczba))

# zadanie 3
if liczba > 100:
    print("Liczba jest większa od 100")
elif 100 >= liczba >= 0:
    print("Liczba jest z przedziału 0 - 100")
else:
    print("Liczba jest mniejsza od 0")

# zadanie 4
cyfra = int(input("Podaj cyfre:"))
match cyfra:
    case 1:
        print("Cyfra 1")
    case 2:
        print("Cyfra 2")
    case 3:
        print("Cyfra 3")
    case 4:
        print("Cyfra 4")
    case 5:
        print("Cyfra 5")
    case 6:
        print("Cyfra 6")
    case 7:
        print("Cyfra 7")
    case 8:
        print("Cyfra 8")
    case 9:
        print("Cyfra 9")
    case 0:
        print("Cyfra 0")
    case _:
        print("Nie podano żadnej cyfry!!!")

# zadanie 5
slonce = input("Czy jest słoneczny dzień? T/N ")
match slonce:
    case "T":
        print("Piękny dzień!")
    case "t":
        print("Piękny dzień!")
    case "N":
        print("Brak słońca!")
    case "n":
        print("Brak słońca!")
    case _:
        print("Podaj poprawną opcję T/N")

# zadanie 6
dzien = input("Podaj dzień tygodnia (z polskimi znakami): ").lower()
match dzien:
    case "poniedziałek":
        print("Jest", dzien)
    case "wtorek":
        print("Jest", dzien)
    case "środa":
        print("Jest", dzien)
    case "czwartek":
        print("Jest", dzien)
    case "piątek":
        print("Jest", dzien)
    case "sobota":
        print("Jest", dzien)
    case "niedziela":
        print("Jest", dzien)
    case _:
        print("Wpisano dzień w złym formacie!")

# zadanie 7
indeks = int(input("Podaj numer indeksu: "))
if indeks % 2 == 0:
    print("Student jest mężczyzną")
else:
    print("Student jest kobietą")

if indeks > 10000:
    print("Studia rozpoczęte w 2019 lub później")
elif 9999 >= indeks >= 9000:
    print("Studia rozpoczęte w 2018")
elif 8999 >= indeks >= 8000:
    print("Studia rozpoczęte w 2017")
elif 7999 >= indeks >= 7000:
    print("Studia rozpoczęte w 2016")
elif 6999 >= indeks >= 6000:
    print("Studia rozpoczęte w 2015")
elif 5999 >= indeks >= 5000:
    print("Studia rozpoczęte w 2014")
elif 4999 >= indeks >= 4000:
    print("Studia rozpoczęte w 2013")
elif 3999 >= indeks >= 3000:
    print("Studia rozpoczęte w 2012")
elif 2999 >= indeks >= 2000:
    print("Studia rozpoczęte w 2011")
elif 1999 >= indeks >= 1000:
    print("Studia rozpoczęte w 2010")
elif indeks < 1000:
    print("Studia rozpoczęte w 2009")

# zadanie 8
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = (b**2)-(4*a*c)
print("Delta wynosi: ", delta)

if delta < 0:
    print("Brak pierwiastków!")
elif delta == 0:
    x = (-b - math.sqrt(delta)) / (2 * a)
    print("Istnieje jeden pierwiastek podwójny ", x)
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("Jeden pierwiastek x1: ", x1, "drugi pierwiastek x2:", x2)