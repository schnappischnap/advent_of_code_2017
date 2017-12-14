from day_10_knot_hash import part_2 as knot_hash


def part_1(data):
    used = 0
    for i in range(128):
        h_hash = knot_hash(data + '-' + str(i))
        used += sum(i == '1' for i in bin(int(h_hash, 16)))
    return used


def part_2(data):
    used = set()
    for i in range(128):
        h_hash = knot_hash(data + '-' + str(i))
        b_hash = bin(int(h_hash, 16))[2:].zfill(128)
        used.update((i, j) for j, b in enumerate(b_hash) if b == '1')

    count = 0
    while used:
        count += 1
        root = next(iter(used))
        to_check = [root]
        while to_check:
            point = to_check.pop()
            if point in used:
                used.remove(point)
                to_check.extend(get_neighbours(point))
    return count


def get_neighbours(point):
    return [(point[0] + dx, point[1] + dy) for dx in range(-1, 2)
                                           for dy in range(-1, 2)
                                           if (dx == 0) ^ (dy == 0)]


if __name__ == '__main__':
    with open('day_14_input.txt') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
