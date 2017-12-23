from collections import defaultdict


def part_1(data):
    registers = defaultdict(int)
    count = 0
    i = 0
    while True:
        if i >= len(data):
            return count

        inst, x, y = data[i].split()
        val_1 = int(x) if is_int(x) else registers[x]
        val_2 = int(y) if is_int(y) else registers[y]

        if inst == 'set':
            registers[x] = val_2
        if inst == 'sub':
            registers[x] -= val_2
        if inst == 'mul':
            registers[x] *= val_2
            count += 1
        if inst == 'jnz':
            if val_1 != 0:
                i += val_2
                continue
        i += 1


def part_2():
    c = 122700
    h = 0
    for b in range(105700, c + 1, 17):
        if not is_prime(b):
            h += 1

    return h


def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False


def is_prime(i):
    return all(i % j for j in range(2, int(i**0.5)))


if __name__ == '__main__':
    with open('day_23_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2()))
