def part_1(data):
    return sum(int(c) for i, c in enumerate(data) if c == data[(i-1)])


def part_2(data):
    shift = len(data)//2
    return sum(int(c) for i, c in enumerate(data) if c == data[(i-shift)])


if __name__ == '__main__':
    with open('day_01_input.txt') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
