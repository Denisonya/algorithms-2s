from random import randint


def generate_input(filename, n, low, high):
    with open(filename, 'w') as f:
        f.write(f'{n}\n')
        f.write(' '.join(str(randint(low, high)) for _ in range(n)) + '\n')
        f.write(' '.join(str(randint(low, high)) for _ in range(n)) + '\n')


# generate_input('input.txt', 1, -10 ** 5, -10 ** 5)
generate_input('input.txt', 10 ** 3, 10 ** 5, 10 ** 5)
