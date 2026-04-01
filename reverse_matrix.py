#   BEFORE:              AFTER:
#   [1, 2, 3]           [3, 2, 1]
#   [4, 5, 6]     →     [6, 5, 4]
#   [7, 8, 9]           [9, 8, 7]


def reverse_matrix(matrix: list) -> list:
    reversed = []

    for li in matrix:
        li.reverse()
        reversed.append(li)

    return reversed


result = reverse_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(result)
