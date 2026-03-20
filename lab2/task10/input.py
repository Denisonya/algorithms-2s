n = 100000

with open('input.txt', 'w') as f:
    f.write(str(n) + '\n')

    for i in range(n):
        if i == n - 1:
            key = 0
        else:
            key = i + 1

        left = 0
        right = i + 2 if i + 1 < n else 0

        f.write(f"{key} {left} {right}\n")
