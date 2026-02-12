from random import randint


def generate_random_array(size: int, left: int, right: int, path: str) -> None:
    """Function to generate random array."""

    random_array = [randint(left, right) for _ in range(size)]
    with open(f"/Users/denisbaranov/cs_projects/1_sem/Algorithms-K25-2025/{path}", "w") as file_output:
        file_output.write(str(size) + "\n")
        file_output.write(" ".join(map(str, random_array)) + "\n")


def find_nearest_prime_number(n: int) -> int:
    """
    Нахождение ближайшего простого числа (большего данного)
    """
    while True:
        n += 1
        is_prime = True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            return n


def is_prime_number(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
