import random
import string

with open("input.txt", "w") as f:
    n = 100000
    letters = string.ascii_lowercase

    s = ''.join(random.choice(letters) for _ in range(n))
    t = ''.join(random.choice(letters) for _ in range(n))

    f.write(f"{s} {t}" + "\n")
