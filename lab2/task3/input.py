import random


def generate_input(filename):
    with open(filename, 'w') as f:
        for _ in range(300_000):
            if random.random() < 0.5:
                x = random.randint(1, 10 ** 9)
                f.write(f"+ {x}\n")
            else:
                x = random.randint(1, 10 ** 9)
                f.write(f"> {x}\n")


generate_input("input.txt")
