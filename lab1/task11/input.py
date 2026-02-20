import random


def generate_input():
    W = 10000
    n = 300

    with open('input.txt', 'w') as f:
        f.write(f'{W} {n}\n')
        for _ in range(n):
            f.write(str(random.randint(1, 10000)) + ' ')


generate_input()
