def part_1(data):
    a, b = (int(line.split()[-1]) for line in data)
    a_gen = gen(a, 16807, 2147483647)
    b_gen = gen(b, 48271, 2147483647)
    return sum(next(a_gen) == next(b_gen) for _ in range(40000000))


def part_2(data):
    a, b = (int(line.split()[-1]) for line in data)
    a_gen = gen(a, 16807, 2147483647, 4)
    b_gen = gen(b, 48271, 2147483647, 8)
    return sum(next(a_gen) == next(b_gen) for _ in range(5000000))


def gen(start, factor, divisor, multiple=1):
    while True:
        start = (start * factor) % divisor
        if start % multiple == 0:
            yield start & 0xFFFF


if __name__ == '__main__':
    with open('day_15_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
