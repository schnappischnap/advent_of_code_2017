import re


def part_1(data):
    pipes = {}
    for line in data:
        a, *b = re.findall(r'(\d+)', line)
        pipes[int(a)] = [int(i) for i in b]

    seen = set()
    follow_pipes(0, seen, pipes)
    return len(seen)


def part_2(data):
    pipes = {}
    for line in data:
        a, *b = re.findall(r'(\d+)', line)
        pipes[int(a)] = [int(i) for i in b]

    seen = set()
    count = 0
    for key in pipes.keys():
        if key not in seen:
            count += 1
            follow_pipes(key, seen, pipes)

    return count


def follow_pipes(prog_id, seen, pipes):
    for prog in pipes[prog_id]:
        if prog not in seen:
            seen.add(prog)
            follow_pipes(prog, seen, pipes)


with open("day_12_input.txt") as f:
    inp = f.readlines()
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))
