def part_1(data):
    chart = [([c for c in line] + [' '] * 200)[:200] for line in data]
    x, y = chart[0].index('|'), 0
    dx, dy = 0, 1
    letters = []

    while True:
        x, y = x+dx, y+dy
        symbol = chart[y][x]

        if symbol == ' ':
            return "".join(letters)
        elif symbol.isalpha():
            letters.append(symbol)
        elif symbol == '+':
            for n in get_neighbours((x, y)):
                if n[0] == x - dx or n[1] == y - dy:
                    continue
                if chart[n[1]][n[0]] == '|' or chart[n[1]][n[0]] == '-':
                    dx, dy = n[0] - x, n[1] - y
                    break


def part_2(data):
    chart = [([c for c in line] + [' ']*200)[:200] for line in data]
    x, y = chart[0].index('|'), 0
    dx, dy = 0, 1
    steps = 0

    while True:
        steps += 1
        x, y = x + dx, y + dy
        symbol = chart[y][x]

        if symbol == ' ':
            return steps
        elif symbol == '+':
            for n in get_neighbours((x, y)):
                if n[0] == x - dx or n[1] == y - dy:
                    continue
                if chart[n[1]][n[0]] == '|' or chart[n[1]][n[0]] == '-':
                    dx, dy = n[0] - x, n[1] - y
                    break


def get_neighbours(point):
    return [(point[0] + dx, point[1] + dy) for dx in range(-1, 2)
                                           for dy in range(-1, 2)
                                           if (dx == 0) ^ (dy == 0)]


if __name__ == '__main__':
    with open('day_19_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
