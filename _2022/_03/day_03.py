def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def part_01(rucksacks: list[str]) -> int:
    priorities = 0

    for rucksack in rucksacks:
        size = len(rucksack)
        first, second = rucksack[: size // 2], rucksack[size // 2 :]
        assert len(first) == len(second)

        repeats = set(first) & set(second)
        assert len(repeats) == 1

        priorities += priority(repeats.pop())

    return priorities


def part_02(rucksacks: list[str]) -> int:
    priorities = 0

    for index in range(0, len(rucksacks), 3):
        group = rucksacks[index : index + 3]
        assert len(group) == 3

        repeats = set(group[0]) & set(group[1]) & set(group[2])
        assert len(repeats) == 1

        priorities += priority(repeats.pop())

    return priorities


def parser(name):
    return list(map(str.strip, open(f"{name}.txt").readlines()))


test_values = parser("test")
input_values = parser("input")

assert part_01(test_values) == 157
assert part_01(input_values) == 8252
print("part_01 =", part_01(input_values))

assert part_02(test_values) == 70
assert part_02(input_values) == 2828
print("part_02 =", part_02(input_values))
