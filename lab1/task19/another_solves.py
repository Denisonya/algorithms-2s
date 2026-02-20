# # v.1 - without restoring the solution
# @time_and_memory_decorator
# def min_operations_for_matrix_multiplication(count_of_matrices, matrices):
#     # cost[i][j] - минимальная стоимость вычисления произведения матриц Ai х ... х Aj,
#     # то есть начиная умножать с Ai и до Aj
#     # cost[i][i] - уже равняется 0 после инициализации таблицы
#     cost = [[0 for _ in range(count_of_matrices)] for _ in range(count_of_matrices)]
#
#     # перебираем размер подзадачи - кол-во матричных операций х (умножить), равное j - i
#     for size in range(1, count_of_matrices):  # 1 2
#         for i in range(count_of_matrices - size):  # 0 1
#             j = i + size
#
#             mn = float('inf')
#             # перебириаем место разбиения, то есть место последнего x (умножения)
#             for k in range(i, j):
#                 split_cost = matrices[i][0] * matrices[k][1] * matrices[j][1]
#                 mn = min(mn, cost[i][k] + cost[k + 1][j] + split_cost)
#
#             cost[i][j] = mn
#
#     return cost[0][count_of_matrices - 1]


# # A - матрица m x n
# # B - матрица k x p
# # по условию все матрицы изначально уже можно умножить, то есть n = k
# # Тогда можно убрать дублирующуюся информацию и упростить индексацию
#
# # v.3 - improves matrix storage
# @time_and_memory_decorator
# def get_optimal_matrix_multiplication_order(count_of_matrices, matrices):
#     sizes_of_matrices = [matrices[0][0]]
#     for a, b in matrices:
#         sizes_of_matrices.append(b)
#     # cost[i][j] - минимальная стоимость вычисления произведения матриц Ai х ... х Aj,
#     # то есть начиная умножать с Ai и до Aj
#     # cost[i][i] - уже равняется 0 после инициализации таблицы
#     cost = [[0 for _ in range(count_of_matrices)] for _ in range(count_of_matrices)]
#
#     # split[i][j] - хранит индекс k матрицы при разбиении (Ai x ... x Ak) x (Ak+1 x ... x Aj)
#     split_table = [[0 for _ in range(count_of_matrices)] for _ in range(count_of_matrices)]
#
#     # перебираем размер подзадачи - кол-во матричных операций х (умножить), равное j - i
#     for size in range(1, count_of_matrices):  # 1 2
#         for i in range(count_of_matrices - size):  # 0 1
#             j = i + size
#
#             mn = float('inf')
#
#             # перебириаем место разбиения, то есть место последнего x (умножения)
#             for k in range(i, j):
#                 split_cost = sizes_of_matrices[i] * sizes_of_matrices[k + 1] * sizes_of_matrices[j + 1]
#                 cur_cost = cost[i][k] + cost[k + 1][j] + split_cost
#
#                 if cur_cost < mn:
#                     mn = cur_cost
#                     split_table[i][j] = k
#
#             cost[i][j] = mn
#
#     return get_order(0, count_of_matrices - 1, split_table)
