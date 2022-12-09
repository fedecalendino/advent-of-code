def make_columns(rows: list[list[int]]) -> list[list[int]]:
    n = len(rows)

    columns = [[0] * n for _ in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            columns[j][i] = rows[i][j]

    return columns


def part_01(rows: list[list[int]]) -> int:
    n = len(rows)
    columns = make_columns(rows)

    visibles = 0

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            tree = rows[i][j]

            up_trees = columns[j][:i]
            if max(up_trees) < tree:
                continue

            down_trees = columns[j][i + 1 :]
            if max(down_trees) < tree:
                continue

            left_trees = rows[i][:j]
            if max(left_trees) < tree:
                continue

            right_trees = rows[i][j + 1 :]
            if max(right_trees) < tree:
                continue

            visibles += 1

    return n * n - visibles


def part_02(rows: list[list[int]]) -> list[list[bool]]:
    def count_visibles(tree: int, trees: list[int]) -> int:
        visibles = 0

        for x in trees:
            visibles += 1

            if x >= tree:
                break

        return visibles

    n = len(rows)
    columns = make_columns(rows)

    best_tree_score = 0

    for i in range(0, n):
        for j in range(0, n):
            tree = rows[i][j]

            up = count_visibles(tree, trees=reversed(columns[j][:i]))
            down = count_visibles(tree, trees=columns[j][i + 1 :])
            left = count_visibles(tree, trees=reversed(rows[i][:j]))
            right = count_visibles(tree, trees=rows[i][j + 1 :])

            best_tree_score = max(
                best_tree_score,
                up * right * down * left,
            )

    return best_tree_score


def parser(name: str) -> str:
    with open(f"{name}.txt") as file:
        rows = []

        for line in file.readlines():
            row = list(map(int, line.strip()))
            rows.append(row)

        return rows


test_values = parser("test")
input_values = parser("input")

assert part_01(test_values) == 21
assert part_01(input_values) == 1835
print("part_01 =", part_01(input_values))

assert part_02(test_values) == 8
assert part_02(input_values) == 263670
print("part_02 =", part_02(input_values))
