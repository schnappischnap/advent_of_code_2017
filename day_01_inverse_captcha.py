def solve_captcha(data, *, part):
    shift = 1 if part == 1 else len(data)//2
    return sum(int(c) for i, c in enumerate(data) if c == data[(i-shift)])


if __name__ == '__main__':
    with open("day_01_input.txt") as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(solve_captcha(inp, part=1)))
        print("Part 2 answer: " + str(solve_captcha(inp, part=2)))
