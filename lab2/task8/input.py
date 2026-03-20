# худший случай - бамбук

n = 2 * 10 ** 5

with open("input.txt", "w") as f:
    f.write(f"{n}\n")
    for i in range(1, n + 1):
        key = i
        left = 0  # нет левого ребенка
        right = i + 1 if i < n else 0  # правый ребенок
        f.write(f"{key} {left} {right}\n")
