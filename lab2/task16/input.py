import random

n = 100_000

with open('input.txt', 'w') as f:
    f.write(str(n) + '\n')

    for _ in range(n):
        cmd = random.randint(-1, 1)

        if cmd == 0:
            k = random.randint(1, 100000)
            f.write(f'0 {k}\n')
        elif cmd == 1:
            number = random.randint(1, 10 ** 9)
            f.write(f'+1 {number}\n')
        else:
            number = random.randint(1, 10 ** 9)
            f.write(f'-1 {number}\n')
