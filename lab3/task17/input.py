import random

N = 300
M = 10 ** 5

with open("input.txt", "w") as f:
    f.write(f"{N} {M}\n")
    for _ in range(M):
        # генерируем случайные города от 1 до N
        a = random.randint(1, N)
        b = random.randint(1, N)
        # не берем ребра из вершины в саму себя, чтобы не был петель
        while b == a:
            b = random.randint(1, N)
        f.write(f"{a} {b}\n")
