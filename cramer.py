from fractions import Fraction


def solve_cramer(m):
    dx = m[0][2] * m[1][1] - m[0][1] * m[1][2]
    dy = m[0][0] * m[1][2] - m[1][0] * m[0][2]
    denominator = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    x = Fraction(dx, denominator)
    y = Fraction(dy, denominator)
    return x, y


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6]]

    solved_matrix = solve_cramer(matrix)

    print(solved_matrix[0], solved_matrix[1])


if __name__ == '__main__':
    main()
