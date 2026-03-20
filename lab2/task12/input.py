# худший случай - бамбук
def generate_input(filename):
    n = 2 * 10 ** 5

    with open(filename, "w") as f:
        f.write(f"{n}\n")
        for i in range(1, n + 1):
            key = i
            left = i + 1 if i < n else 0  # левый ребенок следующий
            right = 0  # правого ребенка нет
            f.write(f"{key} {left} {right}\n")


generate_input("input.txt")
