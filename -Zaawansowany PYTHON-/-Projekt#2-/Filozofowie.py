import threading, time, random, argparse

C_RST = "\033[0m"
C_TITLE = "\033[1;36m"
C_ID = "\033[1;33m"
C_ACTION = "\033[0;37m"
C_OK = "\033[1;32m"

def worker(pid, n, locks, cycles, counts):
    left, right = pid, (pid + 1) % n
    for i in range(1, cycles + 1):
        t = random.uniform(0.05, 0.25)
        print(f"{C_ID}P{pid + 1}{C_ACTION} myśli ({i}/{cycles}) {t:.2f}s{C_RST}")
        time.sleep(t)
        first, second = (left, right) if left < right else (right, left)
        locks[first].acquire()
        locks[second].acquire()
        t = random.uniform(0.02, 0.12)
        print(f"{C_OK}P{pid + 1}{C_ACTION} je pałeczki ({left + 1},{right + 1}) {t:.2f}s{C_RST}")
        time.sleep(t)
        counts[pid] += 1
        locks[second].release()
        locks[first].release()
    print(f"{C_ID}P{pid + 1}{C_ACTION} zakończył (zjadł {counts[pid]} razy){C_RST}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--philosophers", type=int, default=5)
    parser.add_argument("-c", "--cycles", type=int, default=25)
    args = parser.parse_args()

    n = max(2, args.philosophers)
    cycles = max(1, args.cycles)
    locks = [threading.Lock() for _ in range(n)]
    counts = [0] * n

    print(C_TITLE + f"\nSymulacja: {n} filozofów, {cycles} cykli każdy\n" + C_RST)
    start = time.time()

    threads = []
    for i in range(n):
        t = threading.Thread(target=worker, args=(i, n, locks, cycles, counts))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    total = time.time() - start
    print("\n" + C_TITLE + "=" * 35)
    print(" PODSUMOWANIE UCZTY FILOZOFÓW")
    print("=" * 35 + C_RST)
    for i, eaten in enumerate(counts):
        print(f"{C_ID}Filozof {i + 1}:{C_OK} zjadł {eaten} razy{C_RST}")
    print(C_TITLE + f"\nŁączny czas symulacji: {total:.2f}s" + C_RST)
    print("=" * 35 + C_RST)

if __name__ == "__main__":
    main()
