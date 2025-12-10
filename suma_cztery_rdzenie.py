import time
import multiprocessing

def suma_kwadratow(start, end):
    wynik = 0
    for i in range(start, end):
        wynik += i ** 2
    return wynik

def podziel_i_oblicz(start, end, liczba_rdzeni):
    caly_zakres = end - start
    rozmiar_kawalka = caly_zakres // liczba_rdzeni

    zakresy = [
        (start + i * rozmiar_kawalka,
         start + (i + 1) * rozmiar_kawalka)
        for i in range(liczba_rdzeni)
    ]

    if caly_zakres % liczba_rdzeni != 0:
        ostatni_start, _ = zakresy[-1]
        zakresy[-1] = (ostatni_start, end)

    with multiprocessing.Pool(processes=liczba_rdzeni) as pool:
        wyniki = pool.starmap(suma_kwadratow, zakresy)

    return sum(wyniki)

if __name__ == "__main__":
    start_time = time.time()

    start = 1
    end = 10_000_000

    liczba_rdzeni = 4

    wynik = podziel_i_oblicz(start, end, liczba_rdzeni)

    end_time = time.time()

    print(f"Suma kwadratów liczb od {start} do {end - 1}: {wynik}")
    print(f"Czas wykonania na {liczba_rdzeni} rdzeniach: {end_time - start_time:.4f} sekundy")
