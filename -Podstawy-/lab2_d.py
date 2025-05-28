# zadanie 1
liczba = int(input("Podaj liczbę całkowitą: "))
if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba == 0:
    print("Liczba jest równa zero")
else:
    print("Liczba jest ujemna")

# zadanie 2
pkt = int(input("Podaj liczbę punktów 0 - 100: "))
if pkt <= 50:
    print("Ocena 2.0")
elif 50 < pkt <= 60:
    print("Ocena 3.0")
elif 60 < pkt <= 70:
    print("Ocena 3.5")
elif 70 < pkt <= 80:
    print("Ocena 4.0")
elif 80 < pkt <= 90:
    print("Ocena 4.5")
elif 90 < pkt <= 100:
    print("Ocena 5.0")

# zadanie 3
haslo = input("Podaj hasło: ")
if haslo == "password":
    print("Hasło jest poprawne")
else:
    print("Hasło jest niepoprawne")

# zadanie 4
ciag = input("Podaj ciąg znaków: ")
dlugosc = int(input("Podaj długość ciągu: "))
dciag = len(ciag)

if dciag == dlugosc:
    print("Ciąg jest taki sam jak podana długość")
elif dciag > dlugosc:
    print("Ciąg jest dłuższy o ", dciag - dlugosc)
else:
    print("Ciąg jest krótszy o ", dlugosc - dciag)

# zadanie 5
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a**2+b**2==c**2:
    print("Jest to trójka Pitagorejska")
else:
    print("Nie jest to trójka Pitagorejska")

# zadanie 6
p = bool(int(input("Podaj p (0 lub 1): ")))
q = bool(int(input("Podaj q (0 lub 1): ")))

lewa_strona = not (p and q)
prawa_strona = (not p) or (not q)

if lewa_strona == prawa_strona:
    print("Obie strony równania są takie same!")
else:
    print("Strony równania są różne!")

# zadanie 7
dni = int(input("Podaj liczbę dni w hotelu: "))
if dni > 10:
    print("Pobyt kosztuje: ", dni * 150)
elif 5 <= dni <= 10:
    print("Pobyt kosztuje: ", dni * 200)
elif dni < 5:
    print("Pobyt kosztuje: ", dni * 250)
