from collections import defaultdict


def calculate_sizes(output: list[str]) -> dict[str, int]:
    sizes = defaultdict(int)
    current = "/"

    index = 0

    while True:
        index += 1

        if index < len(output):
            line = output[index]
        else:
            if current == "/":
                break

            line = "$ cd .."

        if line.startswith("$ cd"):
            param = line.split(" ")[-1]

            if param == "..":
                size = sizes[current]
                current = "/".join(current.split("/")[:-2] + [""])
                sizes[current] += size
            else:
                current = f"{current}{param}/"
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        else:
            sizes[current] += int(line.split(" ")[0])

    return sizes


def part_01(output: str) -> int:
    sizes = calculate_sizes(output)

    return sum(filter(lambda size: size < 100000, map(int, sizes.values())))


def part_02(output: str) -> int:
    sizes = calculate_sizes(output)

    total = 70000000
    needed = 30000000

    used = sizes["/"]
    unused = total - used

    return min(filter(lambda size: unused + size > needed, sizes.values()))


def parser(name: str) -> str:
    with open(f"{name}.txt") as file:
        return list(map(str.strip, file.readlines()))


test_values = parser("test")
input_values = parser("input")

assert part_01(test_values) == 95437
assert part_01(input_values) == 1084134
print("part_01 =", part_01(input_values))

assert part_02(test_values) == 24933642
assert part_02(input_values) == 6183184
print("part_02 =", part_02(input_values))
