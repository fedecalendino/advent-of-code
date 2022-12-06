def solution(datastream: str, size: int) -> int:
    for i in range(len(datastream)):
        characters = set(datastream[i : i + size])

        if len(characters) == size:
            return i + size


def part_01(datastream: str) -> int:
    return solution(datastream, size=4)


def part_02(datastream: str) -> int:
    return solution(datastream, size=14)


def parser(name: str) -> str:
    with open(f"{name}.txt") as file:
        return file.readline()


test_01_values = parser("test_01")
test_02_values = parser("test_02")
test_03_values = parser("test_03")
test_04_values = parser("test_04")
test_05_values = parser("test_05")
input_values = parser("input")

assert part_01(test_01_values) == 7
assert part_01(test_02_values) == 5
assert part_01(test_03_values) == 6
assert part_01(test_04_values) == 10
assert part_01(test_05_values) == 11
assert part_01(input_values) == 1198
print("part_01 =", part_01(input_values))

assert part_02(test_01_values) == 19
assert part_02(test_02_values) == 23
assert part_02(test_03_values) == 23
assert part_02(test_04_values) == 29
assert part_02(test_05_values) == 26
assert part_02(input_values) == 3120
print("part_02 =", part_02(input_values))
