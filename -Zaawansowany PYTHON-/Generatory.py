# ============================================
# Zadanie 1 - Liczby doskonałe
# ============================================

def generuj_liczby_doskonale():
    n = 2
    while True:
        dzielniki = [i for i in range(1, n) if n % i == 0]
        if sum(dzielniki) == n:
            yield n
        n += 1

gen = generuj_liczby_doskonale()
for _ in range(4):
    print(next(gen))

# ============================================
# Zadanie 2 - N-ty element ciągu arytmetycznego
# ============================================

def ciag_arytmetyczny(a1, r):
    n = 1
    while True:
        yield a1 + (n - 1) * r
        n += 1

gen = ciag_arytmetyczny(5, 5)
for _ in range(5):
    print(next(gen))

# ============================================
# Zadanie 3 - Liczby w postaci binarnej
# ============================================

def liczby_binarne(start, stop):
    for n in range(start, stop + 1):
        yield bin(n)[2:]

print(list(liczby_binarne(3, 6)))

# ============================================
# Zadanie 4 - Liczby Armstronga
# ============================================

def liczby_armstronga():
    n = 1
    while True:
        cyfry = [int(c) for c in str(n)]
        potega = len(cyfry)
        if sum(c ** potega for c in cyfry) == n:
            yield n
        n += 1

gen = liczby_armstronga()
for _ in range(10):
    print(next(gen))

# ============================================
# Zadanie 5 - N-ty element ciągu geometrycznego
# ============================================

def ciag_geometryczny(a1, r):
    a = a1
    while True:
        yield a
        a *= r

gen = ciag_geometryczny(2, 3)
for _ in range(5):
    print(next(gen))

# ============================================
# Zadanie 6 - Liczby w ciągu Fermata
# ============================================

def liczby_fermata():
    n = 0
    while True:
        yield 2 ** (2 ** n) + 1
        n += 1

gen = liczby_fermata()
for _ in range(5):
    print(next(gen))