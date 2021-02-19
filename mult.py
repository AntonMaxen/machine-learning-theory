from gaus import print_matrix


def rotate_matrix(matrix):
    rows = []
    for y in range(len(matrix[0])):
        row = []
        for x in range(len(matrix)):
            row.append(matrix[x][y])

        rows.append(row)

    return rows


def matrix_multiplication(a, b):
    b = rotate_matrix(b)
    sum_matrix = []
    for y in range(len(a)):
        row_one = a[y]
        new_row = []
        for row_two in b:
            total = 0
            for x, n in enumerate(row_two):
                total += (row_one[x] * n)
            new_row.append(total)
        sum_matrix.append(new_row)

    return sum_matrix


def main():
    matrix_one = [[1, 2],
                  [3, 4],
                  [5, 6]]
    matrix_two = [[5, 6, 7],
                  [8, 9, 1]]

    print_matrix(matrix_one)
    print('-' * 5 + f' Multiplicated with ' + '-' * 5)
    print_matrix(matrix_two)

    if len(matrix_one[0]) == len(matrix_two):
        answer = matrix_multiplication(matrix_one, matrix_two)
        print('=' * 5 + ' Equals ' + '=' * 5)
        print_matrix(answer)


if __name__ == '__main__':
    main()
