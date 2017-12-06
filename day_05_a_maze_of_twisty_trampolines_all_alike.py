def calculate_steps(data, *, part):
    instr = list(map(int, data))
    i, steps = 0, 0
    while -1 < i < len(instr):
        steps += 1
        change = 1 if part == 1 or instr[i] < 3 else -1
        instr[i], i = instr[i] + change, i + instr[i]
    return steps


if __name__ == '__main__':
    with open("day_05_input.txt") as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(calculate_steps(inp, part=1)))
        print("Part 2 answer: " + str(calculate_steps(inp, part=2)))