def match_score(opponent: str, mine: str) -> int:
    shape_scores = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    pair_score = {
        ("A", "B"): 6,  # rock vs paper
        ("B", "C"): 6,  # paper vs scissors
        ("C", "A"): 6,  # scissors vs rock
        ("A", "A"): 3,  # rock vs rock
        ("B", "B"): 3,  # paper vs paper
        ("C", "C"): 3,  # scissors vs scissors
        ("A", "C"): 0,  # rock vs scissors
        ("B", "A"): 0,  # paper vs rock
        ("C", "B"): 0,  # scissors vs paper
    }

    return pair_score[opponent, mine] + shape_scores[mine]


def part_01(values: list[tuple[int, int]]) -> int:
    pairs = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    def match(pair: tuple[str, str]) -> int:
        opponent, mine = pair
        return match_score(opponent, pairs[mine])

    return sum(map(match, values))


def part_02(values: list[tuple[int, int]]) -> int:
    pairs = {
        ("A", "X"): "C",
        ("A", "Y"): "A",
        ("A", "Z"): "B",
        ("B", "X"): "A",
        ("B", "Y"): "B",
        ("B", "Z"): "C",
        ("C", "X"): "B",
        ("C", "Y"): "C",
        ("C", "Z"): "A",
    }

    def match(pair: tuple[str, str]) -> int:
        opponent, mine = pair
        return match_score(opponent, pairs[opponent, mine])

    return sum(map(match, values))


def parser(name):
    return list(
        map(
            lambda line: line.strip().split(" "),
            open(f"{name}.txt").readlines(),
        )
    )


test_values = parser("test")
input_values = parser("input")

assert part_01(test_values) == 15
assert part_01(input_values) == 10624
print("part_01 =", part_01(input_values))

assert part_02(test_values) == 12
assert part_02(input_values) == 14060
print("part_02 =", part_02(input_values))
