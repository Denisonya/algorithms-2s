def generate_input():
    n = 1000
    s = 1000

    with open("input.txt", "w") as f:
        f.write(f"{n} {s}\n")

        for i in range(n):
            if i < 500:
                f.write("500 500\n")
            else:
                f.write("500 499\n")


generate_input()
