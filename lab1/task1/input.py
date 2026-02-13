from random import randint


def generate_input(filename, n, W, max_price, max_weight):
    with open(filename, 'w') as f:
        f.write(f'{n} {W}\n')
        for _ in range(n):
            p = randint(0, max_price)
            w = randint(0, max_weight)
            f.write(f'{p} {w}\n')


# generate_input('input.txt', 1, 0, 0, 0)
generate_input('input.txt', 10 ** 3, 2 * 10 ** 6, 2 * 10 ** 6, 2 * 10 ** 6)
