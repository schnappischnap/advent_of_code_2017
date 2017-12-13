def solve(data):
    layers = [tuple(map(int, line.split(":"))) for line in data]
    severity = sum(d*r for d, r in layers if d % ((r - 1) * 2) == 0)

    for i in range(100000000):
        if not any((d + i) % ((r - 1) * 2) == 0 for d, r in layers):
            return severity, i


if __name__ == '__main__':
    with open("day_13_input.txt") as f:
        inp = f.readlines()
        out = solve(inp)
        print("Part 1 answer: " + str(out[0]))
        print("Part 2 answer: " + str(out[1]))
