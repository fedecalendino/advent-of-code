def part_01(stacks, actions) -> str:
    stacks = [list(stack) for stack in stacks]

    for amount, source, target in list(actions):
        items = stacks[source][-amount:]

        stacks[source] = stacks[source][:-amount]
        stacks[target] += items[::-1]

    return "".join(map(lambda stack: stack[-1], stacks))


def part_02(stacks, actions) -> str:
    stacks = [list(stack) for stack in stacks]

    for amount, source, target in list(actions):
        items = stacks[source][-amount:]

        stacks[source] = stacks[source][:-amount]
        stacks[target] += items

    return "".join(map(lambda stack: stack[-1], stacks))


def parser(name):
    with open(f"{name}.txt") as file:
        lines = reversed(file.readlines())

        actions = []

        for line in lines:
            if not line.startswith("move"):
                break

            _, amount, _, source, _, target = line.split(" ")
            actions.insert(0, (int(amount), int(source) - 1, int(target) - 1))

        count = max(map(int, filter(bool, next(lines).split(" "))))

        stacks = [list() for _ in range(count)]

        for line in lines:
            for i in range(count):
                if 4 * i + 1 > len(line):
                    continue

                item = line[4 * i + 1]

                if item != " ":
                    stacks[i].append(item)

        return stacks, actions


test_values = parser("test")
input_values = parser("input")

assert part_01(*test_values) == "CMZ"
assert part_01(*input_values) == "ZSQVCCJLL"
print("part_01 =", part_01(*input_values))

assert part_02(*test_values) == "MCD"
assert part_02(*input_values) == "QZFJRWHGS"
print("part_02 =", part_02(*input_values))
