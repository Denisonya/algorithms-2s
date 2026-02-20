def generate_input(N, K, filename):
    S = ''.join(['a' if i % 2 == 0 else 'b' for i in range(N)])

    with open(filename, "w") as f:
        f.write(f"{N} {K}\n")
        f.write(S + "\n")


generate_input(5000, 0, "input.txt")
