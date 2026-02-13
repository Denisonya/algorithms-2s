def find_nearest_prime_number(n: int) -> int:
    """Нахождение ближайшего простого числа (большего данного)."""
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
    """Проверка числа на простоту."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
