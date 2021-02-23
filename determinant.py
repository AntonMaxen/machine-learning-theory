def solve_two_by_two(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def stbt(matrix):
    return solve_two_by_two(matrix)


def solve_three_by_three(matrix):
    total = 0
    for i, _ in enumerate(matrix):
        prefix = 1
        two_by_two = []
        for j, row in enumerate(matrix):
            if i == j:
                prefix = row[0] if i % 2 != 0 else -row[0]
            else:
                two_by_two.append(row[1:])

        determinant = solve_two_by_two(two_by_two)
        total += prefix * determinant

    return total


def three_by_three_short(matrix):
    total = 0
    for i, current in enumerate(matrix):
        rows = matrix[:i] + matrix[i+1:]
        two_by_two = [row[1:] for row in rows]
        prefix = current[0] if i % 2 != 0 else -current[0]
        total += solve_two_by_two(two_by_two) * prefix

    return total


def three_by_three_shorter(matrix):
    total = 0
    for i, current in enumerate(matrix):
        two_by_two = [row[1:] for j, row in enumerate(matrix) if i != j]
        prefix = current[0] if i % 2 != 0 else -current[0]
        total += solve_two_by_two(two_by_two) * prefix

    return total


def three_by_three_oneline(m):
    return sum([stbt([r[1:] for j, r in enumerate(m) if i != j]) * (c[0] if i % 2 != 0 else -c[0]) for i, c, in enumerate(m)])


def main():
    matrix = [
        [2, -5, 0],
        [3, 1, -4],
        [3, -2, 5]
    ]

    print(three_by_three_shorter(matrix))
    print(three_by_three_oneline(matrix))


if __name__ == '__main__':
    main()
