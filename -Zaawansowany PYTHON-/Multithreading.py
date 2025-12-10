import threading
import time

# ============================================
# Zadanie 1 - Rozgrzewka
# ============================================

def worker(n):
    for _ in range(5):
        print(n, end=" ", flush=True)
        time.sleep(1)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(1, 10)]
for t in threads: t.start()
for t in threads: t.join()

# ============================================
# Zadanie 2 - Stabilność obiektu
# ============================================

class SafeInt:
    def __init__(self, value):
        self.value = value
        self.lock = threading.Lock()

    def update(self, func):
        with self.lock:
            self.value = func(self.value)

x = SafeInt(10)

def add():    x.update(lambda v: v + 5)
def sub():    x.update(lambda v: v - 3)
def mul():    x.update(lambda v: v * 2)
def div():    x.update(lambda v: v // 2)

threads = [threading.Thread(target=f) for f in (add, sub, mul, div)]
for t in threads: t.start()
for t in threads: t.join()
print(x.value)

# ============================================
# Zadanie 3 - Kwadrat liczby v1
# ============================================

import threading

line = input("Podaj liczbę: ")
parts = line.split()
numbers = []
for p in parts:
    numbers.append(int(p))

results = [None] * len(numbers)

def square(i, x):
    results[i] = x * x

threads = []
for i in range(len(numbers)):
    t = threading.Thread(target=square, args=(i, numbers[i]))
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()

print(*results)


# ============================================
# Zadanie 3 - Kwadrat liczby v2
# ============================================

from concurrent.futures import ThreadPoolExecutor

numbers = list(map(int, input("Podaj liczbę: ").split()))
with ThreadPoolExecutor() as pool:
    results = list(pool.map(lambda x: x * x, numbers))

print(*results)

# ============================================
# Zadanie 4 - Liczby pierwsze
# ============================================

numbers = list(map(int, input("Podaj liczbę: ").split()))
results = {}

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def worker(x):
    results[x] = is_prime(x)

threads = [threading.Thread(target=worker, args=(n,)) for n in numbers]
for t in threads: t.start()
for t in threads: t.join()

for n in numbers:
    print(n, "pierwsza" if results[n] else "złożona")


# ============================================
# Zadanie 5 - Lista liczb
# ============================================

shared = []
lock = threading.Lock()

def run(i):
    block = list(range(10*i, 10*i+10))
    with lock:
        shared.extend(block)

threads = [threading.Thread(target=run, args=(i,)) for i in [0,1,2,3]]
for t in threads: t.start()
for t in threads: t.join()
print(shared)


# ============================================
# Zadanie 6 - Pobieranie
# ============================================

from urllib.request import urlopen

urls = [input(f"Podaj URL {i}: ") for i in range(1, 6)]
results = {}

def fetch_all():
    for u in urls:
        with urlopen(u) as r:
            results[u] = len(r.read())

t = threading.Thread(target=fetch_all)
print("Rozpoczynanie pobierania...")
t.start()

while t.is_alive():
    print("Oczekiwanie na zakończenie pobierania...")
    time.sleep(1)

t.join()
print("Wszystko pobrano.")
for u, size in results.items():
    print(f"Liczba znaków dla {u}: {size}")


# ============================================
# Zadanie 7 - Suma kontrolna
# ============================================

import uuid
import hashlib

uuids = [uuid.uuid4().hex for _ in range(200)]
results = {}

def compute(u):
    results[u] = hashlib.md5(u.encode()).hexdigest()

threads = [threading.Thread(target=compute, args=(u,)) for u in uuids]
for t in threads: t.start()
for t in threads: t.join()

for u in uuids:
    print(u, "-", results[u])
