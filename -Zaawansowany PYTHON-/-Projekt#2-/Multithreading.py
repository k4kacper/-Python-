import threading
import time
# ============================================
# Zadanie 1 - Rozgrzewka
# ============================================

def funkcja(n):
    time.sleep(1)
    print(n)

for i in range (1,10):
    t = threading.Thread(target=funkcja,args=(i,))
    t.start()
    t.join()

# ============================================
# Zadanie 2 - Stabilność obiektu
# ============================================

class Dzialania:
    def __init__(self, value=0):
        self.value = value
        self.lock = threading.Lock()
    def add(self, x):
        with self.lock:
            self.value += x
        print(self.value)
    def sub(self,x):
        with self.lock:
            self.value -= x
        print(self.value)
    def mul(self,x):
        with self.lock:
            self.value *= x
        print(self.value)
    def div(self,x):
        with self.lock:
            self.value /= x
        print(self.value)

num = Dzialania(100)

def operacje():
    num.add(5)
    num.sub(10)
    num.mul(10)
    num.div(10)

for i in range(1):
    t = threading.Thread(target=operacje,args=())
    t.start()
    t.join()
# ============================================
# Zadanie 3 - Kwadrat liczby
# ============================================



# ============================================
# Zadanie 4 - Liczby pierwsze
# ============================================

# ============================================
# Zadanie 5 - Lista liczb
# ============================================

# ============================================
# Zadanie 6 - Pobieranie
# ============================================

# ============================================
# Zadanie 7 - Suma kontrolna
# ============================================