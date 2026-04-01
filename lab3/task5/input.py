n = 10 ** 4

with open('input.txt', 'w') as f:
    f.write(f"{n} {n}\n")

    for i in range(1, n):
        f.write(f"{i} {i + 1}\n")

    f.write(f"{n} 1\n")  # замыкаем цикл
