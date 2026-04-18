max_len = 10 ** 4

p = "a"
t = "a" * max_len

with open("input.txt", "w") as f:
    f.write(p + "\n")
    f.write(t + "\n")
