import random

N = 100
commands = ['insert', 'delete', 'exists', 'next', 'prev']

with open('input.txt', 'w') as f:
    for _ in range(N):
        cmd = random.choice(commands)
        x = random.randint(-10**9, 10**9)
        f.write(f"{cmd} {x}\n")