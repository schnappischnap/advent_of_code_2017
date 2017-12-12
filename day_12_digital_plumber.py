import re

pipes = {}


def solve(data):
    for line in data:
        a, *b = re.findall(r'(\d+)', line)
        pipes[int(a)] = [int(i) for i in b]

    seen = set()
    follow_pipes(0, seen)
    part_1 = len(seen)

    seen.clear()
    count = 0
    for key in pipes.keys():
        if key not in seen:
            count += 1
            follow_pipes(key, seen)

    return part_1, count


def follow_pipes(prog_id, seen):
    for prog in pipes[prog_id]:
        if prog not in seen:
            seen.add(prog)
            follow_pipes(prog, seen)


if __name__ == '__main__':
    with open("day_12_input.txt") as f:
        inp = f.readlines()
        out = solve(inp)
        print("Part 1 answer: " + str(out[0]))
        print("Part 2 answer: " + str(out[1]))
