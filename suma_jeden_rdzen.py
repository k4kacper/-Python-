import time

def suma_kwadratow(start, end):
    wynik = 0
    for i in range(start, end):
        wynik += i ** 2
    return wynik

if __name__ == "__main__":
    start_time = time.time()

    start = 1
    end = 10_000_000  # górna granica (nie wliczana w range)

    wynik = suma_kwadratow(start, end)

    end_time = time.time()

    print(f"Suma kwadratów liczb od {start} do {end - 1}: {wynik}")
    print(f"Czas wykonania na jednym rdzeniu: {end_time - start_time:.4f} sekundy")
