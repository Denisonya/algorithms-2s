with open("input.txt", "w") as f:
    n = 100000
    m = n - 1

    f.writelines(f'{n} {m}' + "\n")
    for i in range(1, n):
        f.writelines(f'{i} {i + 1}' + "\n")

    f.writelines(f'{1} {n}' + "\n")
