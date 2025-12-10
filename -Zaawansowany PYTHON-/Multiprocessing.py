import multiprocessing

# ============================================
# Zadanie 1 - Liczba dostępnych procesorów
# ============================================

print("Liczba dostępnych procesorów:", multiprocessing.cpu_count())

# ============================================
# Zadanie 2 - PID
# ============================================

import os
from multiprocessing import Process

def worker():
    print(f"Child PID: {os.getpid()}")

if __name__ == "__main__":
    print(f"Parent PID: {os.getpid()}")

    p1 = Process(target=worker)
    p2 = Process(target=worker)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

# ============================================
# Zadanie 3 - Queue
# ============================================

from multiprocessing import Process, Queue
from time import sleep

def child(q: Queue):
    while True:
        msg = q.get()
        print("Proces potomny:", msg)
        if msg == "exit":
            break

if __name__ == "__main__":
    q = Queue()
    p = Process(target=child, args=(q,))
    p.start()

    while True:
        sleep(1)
        txt = input("Podaj napis: ")
        q.put(txt)
        if txt == "exit":
            break

    q.close()
    q.join_thread()
    p.join()

# ============================================
# Zadanie 4 - Potęga
# ============================================

from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    nums = list(map(int, input("Podaj liczby oddzielone spacją: ").split()))
    with Pool() as pool:
        result = pool.map(square, nums)
    print(*result)

# ============================================
# Zadanie 5 - Liczby pierwsze
# ============================================

from multiprocessing import Pool

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    nums = list(map(int, input("Podaj liczbę: ").split()))
    with Pool() as pool:
        result = pool.map(is_prime, nums)
    for n, r in zip(nums, result):
        print(f"{n}: {'pierwsza' if r else 'złożona'}")


# ============================================
# Zadanie 6 - Suma kontrolna
# ============================================

import uuid
import hashlib
from multiprocessing import Pool

def calc_md5(u: str) -> str:
    return hashlib.md5(u.encode()).hexdigest()

if __name__ == "__main__":
    uuids = [uuid.uuid4().hex for _ in range(200)]

    with Pool() as pool:
        checksums = pool.map(calc_md5, uuids)

    for u, c in zip(uuids, checksums):
        print(f"{u} - {c}")
