def part_1(data):
    rules = {}
    for line in data:
        key, _, val = line.split()
        key = tuple(tuple(c) for c in key.split('/'))
        val = tuple(tuple(c) for c in val.split('/'))

        for perm in permutations(key):
            rules[perm] = val

    pattern = (('.', '#', '.'), ('.', '.', '#'), ('#', '#', '#'))
    for _ in range(5):
        blocks = [rules[block] for block in split(pattern)]
        pattern = stitch(blocks)

    return sum(c == '#' for a in pattern for c in a)


def part_2(data):
    rules = {}
    for line in data:
        key, _, val = line.split()
        key = tuple(tuple(c) for c in key.split('/'))
        val = tuple(tuple(c) for c in val.split('/'))

        for perm in permutations(key):
            rules[perm] = val

    pattern = (('.', '#', '.'), ('.', '.', '#'), ('#', '#', '#'))
    for _ in range(18):
        blocks = [rules[block] for block in split(pattern)]
        pattern = stitch(blocks)

    return sum(c == '#' for a in pattern for c in a)


def permutations(grid):
    grid_cpy = grid[:]
    for _ in range(2):
        for __ in range(4):
            grid_cpy = tuple(zip(*grid_cpy[::-1]))
            yield grid_cpy
        grid_cpy = grid_cpy[::-1]


def split(grid):
    b_len = 2 if len(grid) % 2 == 0 else 3

    for row in range(0, len(grid), b_len):
        for col in range(0, len(grid), b_len):
            yield tuple(grid[y][col:col+b_len] for y in range(row, row+b_len))


def stitch(blocks):
    if len(blocks) == 1:
        return blocks[0]

    g_len = int(len(blocks) ** 0.5)

    grid = []
    for i in range(0, len(blocks), g_len):
        for row in zip(*blocks[i:i+g_len]):
            grid.append(tuple(item for sublist in row for item in sublist))
    return tuple(grid)


if __name__ == '__main__':
    with open('day_21_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
