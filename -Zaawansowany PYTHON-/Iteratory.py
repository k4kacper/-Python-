from itertools import count

# ============================================
# Zadanie 1 - Własny iterator
# ============================================

class Count:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += 1
        return value

counter = count(5)
for i in range(10):
    print(next(counter))

# ============================================
# Zadanie 2 - Tetranacci
# ============================================

class tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.index = 0
        self.sequence = [0, 0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 4:
            result = self.sequence[self.index]
        elif self.index < self.steps:
            next_value = sum(self.sequence[-4:])
            self.sequence.append(next_value)
            result = next_value
        else:
            raise StopIteration
        self.index += 1
        return result

steps = int(input("Podaj liczbę wyrazów ciągu Tetranacciego do wypisania: "))

print("Ciąg Tetranacciego:")
for number in tetranacci(steps):
    print(number)

# ============================================
# Zadanie 3 - Repeat
# ============================================

class repeat:
    def __init__(self, value, times):
        self.value = value
        self.times = times
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.times:
            self.count += 1
            return self.value
        else:
            raise StopIteration


for i in repeat(10, 5):
    print("Powtórz:", i)

# ============================================
# Zadanie 4 - Odd first
# ============================================

class odd_first:
    def __init__(self, iterable):
        self.data = list(iterable)
        self.odd_indices = [i for i in range(len(self.data)) if i % 2 == 1]
        self.even_indices = [i for i in range(len(self.data)) if i % 2 == 0]
        self.indices = self.odd_indices + self.even_indices
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.indices):
            raise StopIteration
        index = self.indices[self.position]
        self.position += 1
        return self.data[index]

lista = ['a', 'b', 'c', 'd', 'e', 'f']
for element in odd_first(lista):
    print(element)
# ============================================
# Zadanie 5 - Chain
# ============================================

class chain:
    def __init__(self, *args):
        self.args = args
        self.iters = [iter(x) for x in args]
        self.current_iter = self.iters.pop(0)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iter)
        except StopIteration:
            if len(self.iters) > 0:
                self.current_iter = self.iters.pop(0)
                return self.__next__()
            else:
                raise StopIteration

for element in chain("ABC", [1, 2, 3], [], "DEF"):
    print(element, end=" ")