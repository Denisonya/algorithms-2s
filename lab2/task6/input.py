n = 100000

with open('input.txt', 'w') as f:
    f.write(str(n) + '\n')

    for i in range(n):
        if i == n - 1:
            key = 0
        else:
            key = i + 1

        left = -1
        right = i + 1 if i + 1 < n else -1
        f.write(f"{key} {left} {right}\n")
