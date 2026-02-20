import random


def generate_input():
    RANKS = '6789TJQKA'
    SUITS = 'SCDH'
    N, M = 35, 4
    trump = random.choice(SUITS)
    cards = [rank + suit for rank in RANKS for suit in SUITS]
    with open("input.txt", "w") as f:
        f.write(f"{N} {M} {trump}\n")
        f.write(' '.join(cards[:N]) + '\n')
        f.write(' '.join(cards[N:N + M]) + '\n')

generate_input()