n = 1000

edges = []

# первая компонента
for i in range(1, n // 2):
    edges.append((i, i + 1))

# вторая компонента
for i in range(501, n - 1):
    edges.append((i, i + 1))

m = len(edges)

with open("input.txt", "w") as f:
    f.write(f"{n} {m}\n")

    for a, b in edges:
        f.write(f"{a} {b}\n")

    f.write("1 1000\n")
