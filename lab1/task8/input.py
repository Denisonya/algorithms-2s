from random import randint


def generate_input(filename, n):
    with open(filename, 'w') as f:
        f.write(f'{n}\n')
        for _ in range(n):
            start = randint(1, 1439)
            finish = randint(start + 1, 1440)
            f.write(f'{start} {finish}\n')


generate_input('input.txt', 1000)
