import random


def generate_input(filename):
    with open(filename, 'w') as f:
        n = 300_000

        # вставки
        for _ in range(n // 2):
            x = random.randint(1, 10 ** 9)
            f.write(f"+ {x}\n")

        current_size = n // 2

        # запросы
        for _ in range(n // 2):
            k = random.randint(1, current_size)
            f.write(f"? {k}\n")


generate_input("input.txt")
