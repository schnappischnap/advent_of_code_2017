def part_1(data):
    instructions = data.split(',')
    progs = list('abcdefghijklmnop')

    for ins in instructions:
        if ins[0] == 's':
            amount = int(ins[1:])
            progs = progs[-amount:] + progs[:-amount]
        if ins[0] == 'x':
            pos1, pos2 = map(int, ins[1:].split('/'))
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]
        if ins[0] == 'p':
            prog1, prog2 = ins[1], ins[3]
            pos1, pos2 = progs.index(prog1), progs.index(prog2)
            progs[pos1], progs[pos2] = prog2, prog1

    return "".join(progs)


def part_2(data):
    instructions = data.split(',')
    progs = list('abcdefghijklmnop')
    seen = []

    for i in range(1000000000):
        if progs in seen:
            return "".join(seen[1000000000 % i])
        seen.append(progs[:])

        for ins in instructions:
            if ins[0] == 's':
                amount = int(ins[1:])
                progs = progs[-amount:] + progs[:-amount]
            if ins[0] == 'x':
                pos1, pos2 = map(int, ins[1:].split('/'))
                progs[pos1], progs[pos2] = progs[pos2], progs[pos1]
            if ins[0] == 'p':
                prog1, prog2 = ins[1], ins[3]
                pos1, pos2 = progs.index(prog1), progs.index(prog2)
                progs[pos1], progs[pos2] = prog2, prog1


if __name__ == '__main__':
    with open('day_16_input.txt') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
