from collections import defaultdict


def part_1(data):
    registers = defaultdict(int)

    for line in data:
        reg1, change, val1, _, reg2, op, val2 = line.split()

        if eval(str(registers[reg2]) + op + val2):
            registers[reg1] += int(val1) * (1 if change == 'inc' else -1)

    return max(registers.values())


def part_2(data):
    registers = defaultdict(int)
    largest = 0

    for line in data:
        reg1, change, val1, _, reg2, op, val2 = line.split()

        if eval(str(registers[reg2]) + op + val2):
            registers[reg1] += int(val1) * (1 if change == 'inc' else -1)
            largest = max(largest, registers[reg1])

    return largest


if __name__ == '__main__':
    with open('day_08_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 1 answer: " + str(part_2(inp)))
