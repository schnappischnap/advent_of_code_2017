def part_1(data):
    instr = list(map(int, data))
    i, steps = 0, 0
    while -1 < i < len(instr):
        steps += 1
        change = 1
        instr[i], i = instr[i] + change, i + instr[i]
    return steps


def part_2(data):
    instr = list(map(int, data))
    i, steps = 0, 0
    while -1 < i < len(instr):
        steps += 1
        change = 1 if instr[i] < 3 else -1
        instr[i], i = instr[i] + change, i + instr[i]
    return steps


if __name__ == '__main__':
    with open('day_05_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
