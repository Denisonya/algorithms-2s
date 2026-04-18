max_len = 10**6

p = "a" * (max_len - 1) + "b"
t = "a" * max_len

with open("input.txt", "w") as f:
    f.write(p + "\n")
    f.write(t + "\n")