def calc_crossproduct(u, v):
    matrix = change_orientation([[1, 1, 1], u, v])
    return vector_product(matrix)


def solve_two_by_two(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def change_orientation(m):
    return [[m[0][i], m[1][i], m[2][i]] for i, _ in enumerate(m)]


def vector_product(matrix):
    coord = []
    for i, current in enumerate(matrix):
        two_by_two = [row[1:] for j, row in enumerate(matrix) if i != j]
        prefix = current[0] if i % 2 == 0 else -current[0]
        coord.append(solve_two_by_two(two_by_two) * prefix)

    return coord


def main():
    one = [1, 2, 3]
    two = [4, 5, 6]
    cross_product = calc_crossproduct(one, two)
    print(cross_product)


if __name__ == '__main__':
    main()
