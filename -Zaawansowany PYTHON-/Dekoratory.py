# ============================================
# Zadanie 1 - Hello
# ============================================

def hello(func):
    def wrapper(*args, **kwargs):
        print("hello")
        return func(*args, **kwargs)
    return wrapper

@hello
def moja_funkcja():
    print("moja funkcja")

print("\n--- TEST ZADANIE 1 ---")
moja_funkcja()
moja_funkcja()


# ============================================
# Zadanie 2 - Tetranacci (rekurencyjnie)
# ============================================

def tetranacci(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 0
    elif n == 3:
        return 1
    return (tetranacci(n-1) +
            tetranacci(n-2) +
            tetranacci(n-3) +
            tetranacci(n-4))

print("\n--- TEST ZADANIE 2 ---")
print("Tetranacci(10) =", tetranacci(10))


# ============================================
# Zadanie 2.1 - Tetranacci cache
# ============================================

def cache(func):
    memo = {}
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper

@cache
def tetranacci_cached(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 0
    elif n == 3:
        return 1
    return (tetranacci_cached(n-1) +
            tetranacci_cached(n-2) +
            tetranacci_cached(n-3) +
            tetranacci_cached(n-4))

print("\n--- TEST ZADANIE 2.1 ---")
print("Tetranacci cached(30) =", tetranacci_cached(30))


# ============================================
# Zadanie 3 - Nazwa funkcji
# ============================================

def debug_name(func):
    def wrapper(*args, **kwargs):
        print(f"DEBUG: {func.__name__} function called")
        return func(*args, **kwargs)
    return wrapper

@debug_name
def first_function():
    return 1

@debug_name
def second_function(a, b, c):
    return a + b + c

print("\n--- TEST ZADANIE 3 ---")
print(first_function())
print(second_function(1, 2, 3))


# ============================================
# Zadanie 3.1 - Argumenty funkcji
# ============================================

def debug_args(func):
    def wrapper(*args, **kwargs):
        print(f"DEBUG: {func.__name__} function called with {len(args)} args:")
        for i, arg in enumerate(args):
            print(f"DEBUG: {func.__name__} function called <arg{i}> = {arg}")
        print(f"DEBUG: {func.__name__} function called with {len(kwargs)} kwargs:")
        for k, v in kwargs.items():
            print(f"DEBUG: {func.__name__} function called {k} = {v}")
        return func(*args, **kwargs)
    return wrapper

@debug_args
def third_function(a, b, c=3):
    return a + b + c

print("\n--- TEST ZADANIE 3.1 ---")
print(third_function(1, 2, c=3))


# ============================================
# Zadanie 3.2 - Wartość zwracana
# ============================================

def debug_full(func):
    def wrapper(*args, **kwargs):
        print(f"DEBUG: {func.__name__} function called with {len(args)} args:")

        for i, arg in enumerate(args):
            print(f"DEBUG: {func.__name__} function called <arg{i}> = {arg}")

        print(f"DEBUG: {func.__name__} function called with {len(kwargs)} kwargs:")
        for k, v in kwargs.items():
            print(f"DEBUG: {func.__name__} function called {k} = {v}")

        result = func(*args, **kwargs)

        print(f"DEBUG: {func.__name__} function called returned value: {result}")
        return result
    return wrapper

@debug_full
def first_function():
    return 1

@debug_full
def second_function(a, b, c):
    return a + b + c

@debug_full
def third_function(a, b, c=3):
    return a + b + c

print("\n--- TEST ZADANIE 3.2 ---")
print(first_function())
print(second_function(1, 2, 3))
print(third_function(1, 2, c=3))


# ============================================
# Zadanie 4 - Profiling
# ============================================

import time

def profiling(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"DEBUG: {func.__name__} function execution took: {end - start:.6f} seconds")
        return result
    return wrapper

@profiling
def slow_function():
    time.sleep(0.1)
    return "done"

print("\n--- TEST ZADANIE 4 ---")
print(slow_function())
print(slow_function())


# ============================================
# Zadanie 5 - Łączenie dekoratorów
# ============================================

@profiling
@debug_name
def combined_function():
    sum([i for i in range(100000)])

print("\n--- TEST ZADANIE 5 ---")
combined_function()


# ============================================
# Zadanie 6 - Login required
# ============================================

class NotLoggedIn(Exception):
    pass

logged_in_user = None

def login_required(func):
    def wrapper(*args, **kwargs):
        if logged_in_user:
            return func(*args, **kwargs)
        else:
            raise NotLoggedIn("Musisz się zalogować")
    return wrapper

def login():
    global logged_in_user
    user = input("uzytkownik: ")
    if user == "anonim":
        logged_in_user = None
    else:
        password = input("haslo: ")
        if user == "jan" and password == "kowalski":
            logged_in_user = user
        else:
            logged_in_user = None

@login_required
def hello_login():
    print("Hello")

print("\n--- TEST ZADANIE 6 ---")

login()
hello_login()