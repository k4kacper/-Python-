# # Zadanie 2
# def suma(n):
#     if n == 1:
#         return 1
#     else:
#         return n + suma(n - 1)
#
# n = int(input("Podaj ilość liczb do zsumowania: "))
# print("Suma wynosi: ", suma(n))

# # Zadanie 3
# def suma_cyfr(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + suma_cyfr(n // 10)
#
# n = int(input("Podaj liczbe: "))
# print("Suma cyfr wynosi: ", suma_cyfr(n))

# # Zadanie 4
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# n = int(input("Podaj któy element ciągu wyznaczyć: "))
# print("Ciąg Fibonacciego: ", fib(n))

# # Zadanie 5
# def nwd_rek(a, b):
#     if b == 0:
#         return a
#     else:
#         return nwd_rek(b, a % b)
#
# a = int(input("Podaj a:"))
# b = int(input("Podaj b:"))
# print("NWD wynosi: ", nwd_rek(a, b))

# # Zadanie 6
# def nwd_it(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
#
# a = int(input("Podaj a:"))
# b = int(input("Podaj b:"))
# print("NWD wynosi: ", nwd_it(a, b))

# # Zadanie 7
# def ciag_a(x,y,z):
#     if z == 1:
#         return x
#     else:
#         return ciag_a(x,y,z-1) + y
#
# x = int(input("Podaj pierwszy element ciągu: "))
# y = int(input("Podaj krok ciągu: "))
# z = int(input("Podaj ilość elementów ciągu: "))
# print("Ostatni element ciągu arytmetycznego: ", ciag_a(x,y,z))

# Zadanie 8
def ciag_g(x,y,z):
    if z == 1:
        return x
    else:
        return ciag_g(x,y,z-1) * y

x = int(input("Podaj pierwszy element ciągu: "))
y = int(input("Podaj krok ciągu: "))
z = int(input("Podaj ilość elementów ciągu: "))
print("Ostatni element ciągu geometrycznego: ", ciag_g(x,y,z))