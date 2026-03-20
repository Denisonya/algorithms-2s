# худший случай - бамбук
def generate_input(filename):
    n = 10 ** 5
    with open(filename, "w") as f:
        f.write(f"{n}\n")
        for i in range(n):
            key = i + 1
            left = i + 1 if i + 1 < n else -1  # левый ребенок следующий
            right = -1  # правого ребенка нет
            f.write(f"{key} {left} {right}\n")


generate_input("input.txt")
