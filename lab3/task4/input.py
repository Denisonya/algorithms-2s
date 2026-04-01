with open('input.txt', 'w') as f:
    n = 10 ** 5
    m = n - 1

    f.write(f'{n} {m}\n')
    for i in range(1, n):
        f.write(f'{i} {i + 1}\n')
