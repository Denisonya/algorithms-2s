def generate_input(filename):
    n = 400
    with open(filename, 'w') as f:
        f.write(f'{n}\n')
        for _ in range(n):
            f.write('100 100\n')


generate_input('input.txt')
