import random

with open("input.txt") as f:
    n = 1000
    m = 1000

    edges = set()

    while len(edges) < m:
        a = random.randint(1, n)
        b = random.randint(1, n)
        if a != b:
            edges.add((a, b))

    f.write(f'{n} {m}\n')
    for a, b in edges:
        f.write(f'{a} {b}\n')
