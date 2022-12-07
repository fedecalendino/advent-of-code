def calories_per_elf(values: list[str]) -> list[int]:
    elf = 0

    for value in values:
        if value:
            elf += int(value)
        else:
            yield elf
            elf = 0

    yield elf


def part_01(values: list[str]) -> int:
    return max(calories_per_elf(values))


def part_02(values: list[str]) -> int:
    return sum(sorted(calories_per_elf(values), reverse=True)[:3])


def parser(name):
    with open(f"{name}.txt") as file:
        return list(map(str.strip, file.readlines()))


test_values = parser("test")
input_values = parser("input")


assert part_01(test_values) == 24000
assert part_01(input_values) == 70698
print("part_01 =", part_01(input_values))


assert part_02(test_values) == 45000
assert part_02(input_values) == 206643
print("part_02 =", part_02(input_values))
