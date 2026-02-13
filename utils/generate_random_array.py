from random import randint


def generate_random_array(size: int, left: int, right: int, path: str) -> None:
    """Function to generate random array."""

    random_array = [randint(left, right) for _ in range(size)]
    with open(f"/Users/denisbaranov/cs_projects/1_sem/Algorithms-K25-2025/{path}", "w") as file_output:
        file_output.write(str(size) + "\n")
        file_output.write(" ".join(map(str, random_array)) + "\n")
