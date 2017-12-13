def part_1(data):
    layers = [tuple(map(int, line.split(":"))) for line in data]
    return sum(d*r for d, r in layers if d % ((r - 1) * 2) == 0)


def part_2(data):
    layers = [tuple(map(int, line.split(":"))) for line in data]
    for i in range(100000000):
        if not any((d + i) % ((r - 1) * 2) == 0 for d, r in layers):
            return i


with open("day_13_input.txt") as f:
    inp = f.readlines()
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))
