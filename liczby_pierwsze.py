import time
import multiprocessing as mp
from math import sqrt


def is_prime(n):
    """Sprawdza czy liczba jest pierwsza (wolna metoda dla lepszej demonstracji)"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(start, end):
    """Liczy liczby pierwsze w podanym zakresie [start, end)"""
    count = 0
    for num in range(start, end):
        if is_prime(num):
            count += 1
    return count


def single_core_computation(n):
    """Obliczenia na jednym rdzeniu"""
    print(f"\n{'=' * 60}")
    print(f"OBLICZENIA NA JEDNYM RDZENIU")
    print(f"{'=' * 60}")

    start_time = time.time()
    result = count_primes_in_range(1, n)
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"Znaleziono {result} liczb pierwszych")
    print(f"Czas wykonania: {elapsed:.2f} sekund")
    return elapsed


def multi_core_computation(n, num_cores):
    """Obliczenia na wielu rdzeniach"""
    print(f"\n{'=' * 60}")
    print(f"OBLICZENIA NA {num_cores} RDZENIACH")
    print(f"{'=' * 60}")

    chunk_size = n // num_cores
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_cores)]
    ranges[-1] = (ranges[-1][0], n)

    start_time = time.time()

    with mp.Pool(processes=num_cores) as pool:
        results = pool.starmap(count_primes_in_range, ranges)

    total_primes = sum(results)
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"Znaleziono {total_primes} liczb pierwszych")
    print(f"Czas wykonania: {elapsed:.2f} sekund")
    return elapsed


def main():
    N = 200_000

    print(f"\n TEST WYDAJNOŚCI - Szukanie liczb pierwszych do {N}")
    print(f"Dostępne rdzenie CPU: {mp.cpu_count()}")

    time_1_core = single_core_computation(N)

    time_2_cores = multi_core_computation(N, 2)

    num_cores = min(4, mp.cpu_count())
    time_4_cores = multi_core_computation(N, num_cores)


    print(f"\n{'=' * 60}")
    print(f" PODSUMOWANIE")
    print(f"{'=' * 60}")
    print(f"1 rdzeń:        {time_1_core:.2f}s")
    print(f"2 rdzenie:      {time_2_cores:.2f}s  (przyspieszenie: {time_1_core / time_2_cores:.2f}x)")
    print(f"{num_cores} rdzenie:  {time_4_cores:.2f}s  (przyspieszenie: {time_1_core / time_4_cores:.2f}x)")
    print(f"\n Oszczędność czasu:")
    print(f"   2 rdzenie:      {time_1_core - time_2_cores:.2f}s ({(1 - time_2_cores / time_1_core) * 100:.1f}%)")
    print(f"   {num_cores} rdzenie: {time_1_core - time_4_cores:.2f}s ({(1 - time_4_cores / time_1_core) * 100:.1f}%)")


if __name__ == "__main__":
    main()
