from fractions import Fraction


def get_pivot_index(matrix, current_stair):
    highest = 0
    for i in range(len(matrix)):
        new_value = abs(matrix[i][current_stair])
        old_value = abs(matrix[highest][current_stair])
        highest = i if new_value > old_value else highest

    return highest


def make_row_one(matrix_row, current_stair):
    divider = matrix_row[current_stair]
    return [Fraction(value, divider) for value in matrix_row]


def make_rows_zero(matrix, current_stair):
    new_matrix = []
    for i, row in enumerate(matrix):
        if i != current_stair:
            base = matrix[current_stair]
            tower = row[current_stair]
            multiplier = tower * -1
            modified_row = [n * multiplier for n in base]
            new_row = [modified_row[i] + row[i] for i in range(len(row))]
        else:
            new_row = row

        new_matrix.append(new_row)

    return new_matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(num) for num in row]))


def solve_gauss(matrix):
    unknows = len(matrix)
    for i in range(unknows):
        current_stair = i
        # get number based in index
        highest = get_pivot_index(matrix, current_stair)
        # swap
        matrix[current_stair], matrix[highest] = matrix[highest], matrix[current_stair]
        # make column index 1
        one_row = make_row_one(matrix[current_stair], current_stair)
        matrix[current_stair] = one_row
        # make other columns 0
        matrix = make_rows_zero(matrix, current_stair)
        print('=' * 10 + f' column: {current_stair} ' + '=' * 10)
        print_matrix(matrix)

    return matrix


def main():
    matrix_one = [
        [3, 5, 9, 2],
        [2, 7, 2, 6],
        [4, 3, 3, 9]
    ]

    matrix_two = [
        [33, 3, -9, 3],
        [3, 77, 5, 5],
        [7, 2, 2, 7]
    ]

    matrix = matrix_two

    print('#' * 10 + " starting with matrix " + '#' * 10)
    print_matrix(matrix)
    solved_matrix = solve_gauss(matrix)
    print('#' * 10 + " the solved matrix is " + '#' * 10)
    print_matrix(solved_matrix)


if __name__ == '__main__':
    main()
