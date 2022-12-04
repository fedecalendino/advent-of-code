def part_01(assignments: list[tuple, tuple]) -> int:
    total_overlaps = 0

    for (first_start, first_end), (second_start, second_end) in assignments:
        if first_start <= second_start and second_end <= first_end:
            total_overlaps += 1
        elif second_start <= first_start and first_end <= second_end:
            total_overlaps += 1

    return total_overlaps


def part_02(assignments: list[tuple, tuple]) -> int:
    total_overlaps = 0

    for (first_start, first_end), (second_start, second_end) in assignments:
        if first_start > second_end:
            continue

        if second_start > first_end:
            continue

        total_overlaps += 1

    return total_overlaps


def parser(name):
    for line in open(f"{name}.txt").readlines():
        first, second = line.strip().split(",")

        first = tuple(map(int, first.split("-")))
        second = tuple(map(int, second.split("-")))
        assert len(first) == len(second) == 2

        first_start, first_end = first
        second_start, second_end = second
        assert first_start <= first_end
        assert second_start <= second_end

        yield (first_start, first_end), (second_start, second_end)


test_values = list(parser("test"))
input_values = list(parser("input"))

assert part_01(test_values) == 2
assert part_01(input_values) == 459
print("part_01 =", part_01(input_values))

assert part_02(test_values) == 4
assert part_02(input_values) == 779
print("part_02 =", part_02(input_values))
