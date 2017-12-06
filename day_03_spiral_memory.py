def calculate_spiral(data, *, part):
    goal = int(data)
    x, y = 1, 0
    dx, dy = 1, 0
    steps = 1           # part 1
    grid = {(0, 0): 1}  # part 2

    while True:
        steps += 1
        total = sum(grid[n] for n in get_neighbours((x, y)) if n in grid)
        grid[(x, y)] = total

        if part == 1 and steps == goal:
            return abs(x) + abs(y)
        if part == 2 and total > goal:
            return total

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def get_neighbours(point):
    return [(point[0] + dx, point[1] + dy) for dx in range(-1, 2)
                                           for dy in range(-1, 2)
                                           if not (dx == 0 and dy == 0)]


if __name__ == '__main__':
    with open("day_03_input.txt") as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(calculate_spiral(inp, part=1)))
        print("Part 2 answer: " + str(calculate_spiral(inp, part=2)))
