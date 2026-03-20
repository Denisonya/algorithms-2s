import random


def generate_input(filename):
    n = 100_000
    M = 1_000_000_001

    with open(filename, "w") as f:
        f.write(f"{n}\n")

        last_sum = 0
        current_set = set()

        # чередуем добавление новых больших чисел и суммирование всего диапазона
        for i in range(n):
            if i % 5 == 0:
                # добавление новых чисел
                num = (10 ** 9 - i) % M
                f.write(f"+ {num}\n")
                current_set.add(num)
            elif i % 5 == 1:
                # удаление случайного элемента
                if current_set:
                    num = random.choice(list(current_set))
                    f.write(f"- {num}\n")
                    current_set.remove(num)
                else:
                    f.write(f"- {i}\n")  # удаляем несуществующее
            elif i % 5 == 2:
                # поиск существующего числа
                if current_set:
                    num = random.choice(list(current_set))
                    f.write(f"? {num}\n")
                else:
                    f.write(f"? {i}\n")
            else:
                # суммирование всего диапазона
                f.write(f"s 0 1000000000\n")


generate_input("input.txt")
