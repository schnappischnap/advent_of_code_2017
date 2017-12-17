def part_1(data):
    steps = int(data)
    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos = ((pos + steps) % len(buffer)) + 1
        buffer.insert(pos, i)
    return buffer[pos + 1]


def part_2(data):
    steps = int(data)
    buffer_len = 1
    pos = 0
    at_pos_1 = 0
    for i in range(1, 50000001):
        pos = ((pos + steps) % buffer_len) + 1
        buffer_len += 1
        if pos == 1:
            at_pos_1 = i
    return at_pos_1


if __name__ == '__main__':
    with open('day_17_input.txt') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
