def part_1(data):
    blocks = list(map(int, data.split()))
    seen = {}
    steps = 0

    while tuple(blocks) not in seen:
        seen[tuple(blocks)] = steps
        steps += 1

        index, count = max(enumerate(blocks), key=lambda k: (k[1]))
        blocks[index] = 0
        for i in range(1, count + 1):
            blocks[(index + i) % len(blocks)] += 1

    return steps


def part_2(data):
    blocks = list(map(int, data.split()))
    seen = {}
    steps = 0

    while tuple(blocks) not in seen:
        seen[tuple(blocks)] = steps
        steps += 1

        index, count = max(enumerate(blocks), key=lambda k: (k[1]))
        blocks[index] = 0
        for i in range(1, count + 1):
            blocks[(index + i) % len(blocks)] += 1

    return steps - seen[tuple(blocks)]


with open("day_06_input.txt") as f:
    inp = f.readlines()[0]
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))
