def part_1(data):
    goal = int(data)
    x, y = 1, 0
    dx, dy = 1, 0
    steps = 1

    while True:
        steps += 1

        if steps == goal:
            return abs(x) + abs(y)

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def part_2(data):
    goal = int(data)
    x, y = 1, 0
    dx, dy = 1, 0
    grid = {(0, 0): 1}

    while True:
        total = sum(grid[n] for n in get_neighbours((x, y)) if n in grid)
        grid[(x, y)] = total

        if total > goal:
            return total

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def get_neighbours(point):
    return [(point[0] + dx, point[1] + dy) for dx in range(-1, 2)
                                           for dy in range(-1, 2)
                                           if not (dx == 0 and dy == 0)]


if __name__ == '__main__':
    with open('day_03_input.txt') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
