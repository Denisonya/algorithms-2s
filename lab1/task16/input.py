def generate_input(filename, n):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        for i in range(n):
            for j in range(n):
                if i == j:
                    f.write("0 ")
                else:
                    f.write("1000000 ")
            f.write("\n")


generate_input("input.txt", 13)
