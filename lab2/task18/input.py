def generate_input(filename):
    n = 300_000
    count = 100_000

    # формируем строку
    s = ''
    for i in range(n):
        s += chr(ord('a') + i % 26)

    with open(filename, "w") as f:
        f.write(s + "\n")
        f.write(str(count) + "\n")

        # каждый раз вырезаем первый символ и вставляем в конец
        for _ in range(count):
            f.write(f"0 0 {n - 1}\n")


generate_input("input.txt")
