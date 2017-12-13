def part_1(data):
    blah = {"n": (0, 1),  "ne": (1, 0),  "se": (1, -1),
            "s": (0, -1), "sw": (-1, 0), "nw": (-1, 1)}
    x, y = 0, 0

    for step in data.split(","):
        x, y = x + blah[step][0], y + blah[step][1]
        distance = (abs(x) + abs(y) + abs(-x-y)) // 2

    return distance


def part_2(data):
    blah = {"n": (0, 1),  "ne": (1, 0),  "se": (1, -1),
            "s": (0, -1), "sw": (-1, 0), "nw": (-1, 1)}
    x, y = 0, 0
    max_distance = 0

    for step in data.split(","):
        x, y = x + blah[step][0], y + blah[step][1]
        distance = (abs(x) + abs(y) + abs(-x-y)) // 2
        max_distance = max(max_distance, distance)

    return max_distance


with open("day_11_input.txt") as f:
    inp = f.readlines()[0]
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))