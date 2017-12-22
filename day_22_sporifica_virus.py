from collections import defaultdict


def part_1(data):
    cells = defaultdict(int)
    for i, line in enumerate(data):
        for j, c in enumerate(line.strip()):
            if c == '#':
                cells[(j, i)] = 1

    x, y = 12, 12
    dx, dy = 0, -1

    count = 0
    for _ in range(10000):
        if cells[(x, y)] == 1:  # Clean
            dx, dy = -dy, dx
        else:                   # Infected
            dx, dy = dy, -dx
            count += 1

        cells[(x, y)] = (cells[(x, y)] + 1) % 2
        x, y = x + dx, y + dy

    return count


def part_2(data):
    cells = defaultdict(int)
    for i, line in enumerate(data):
        for j, c in enumerate(line.strip()):
            if c == '#':
                cells[(j, i)] = 2

    x, y = 12, 12
    dx, dy = 0, -1

    count = 0
    for _ in range(10000000):
        if cells[(x, y)] == 0:    # Clean
            dx, dy = dy, -dx
        elif cells[(x, y)] == 2:  # Infected
            dx, dy = -dy, dx
        elif cells[(x, y)] == 3:  # Flagged
            dx, dy = -dx, -dy
        else:                     # Weakened
            count += 1

        cells[(x, y)] = (cells[(x, y)] + 1) % 4
        x, y = x + dx, y + dy

    return count


if __name__ == '__main__':
    with open('day_22_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
