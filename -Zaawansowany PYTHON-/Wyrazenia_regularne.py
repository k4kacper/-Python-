import re

# ============================================
# Zadanie 1 - Sprawdzanie czy napis jest liczbą
# ============================================

napis = input("Podaj napis: ")
wynik = re.search("[a-zA-Z]", napis)
if wynik:
    print("To nie jest liczba")
else:
    print("To jest liczba")

# ============================================
# Zadanie 2 - Wyszukiwanie cyfr
# ============================================

napis = input("Podaj napis: ")
wynik = re.findall("[0-9]", napis)

print("Znalezione liczby",wynik)

# ============================================
# Zadanie 3 - Sprawdzanie kolorów
# ============================================

kolor = input("Podaj kolor: ")
wynik = re.match("#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}", kolor)

if wynik:
    print("Zapis poprawny")
else:
    print("Zapis nie poprawny")

# ============================================
# Zadanie 4 - Sprawdzanie kodów pocztowych
# ============================================

kod = input("Podaj kod pocztowy:")
wynik = re.match("^[0-9]{2}-[0-9]{3}$",kod)

if wynik:
    print("Poprawny zapis kodu pocztowego")
else:
    print("Nie poprawny zapis kodu pocztowego")

# ============================================
# Zadanie 5 - Sprawdzanie adresów email
# ============================================

email = input("Podaj email:")
wynik = re.match(".*@.*[.].{2,}",email)

if wynik:
    print("Poprawny adres mailowy")
else:
    print("Nie poprawny adres mailowy")