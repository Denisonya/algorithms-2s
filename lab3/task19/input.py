import random

n = 200
k = 200

points = set()

# генерируем уникальные точки
while len(points) < n:
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    points.add((x, y))

points = list(points)

with open('input.txt', "w") as f:
    f.write(str(n) + "\n")

    for x, y in points:
        f.write(f"{x} {y}\n")

    f.write(str(k) + "\n")
