import random

with open('input.txt', 'w') as f:
    n = 10000
    m = 100000

    f.write(f'{n} {m}\n')

    for _ in range(m):
        a = random.randint(1, n)
        b = random.randint(1, n)
        while a == b:
            b = random.randint(1, n)
        w = random.randint(1, 10 ** 8)
        f.write(f'{a} {b} {w}\n')

    f.writelines(f'{1} {n}\n')
