with open('input.txt', 'w') as f:
    n = 200
    f.write(str(n) + '\n')

    x = -1000
    y = -1000

    for i in range(n):
        f.write(f'{x} {y}\n')
        x += 10
        if x > 1000:
            x = -1000
            y += 10
