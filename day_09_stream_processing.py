import re


def part_1(data):
    a = re.sub(r'!\S', '', data)  # Remove '!' and cancelled
    b = re.sub(r'<[^>]*>', '', a)  # Remove garbage

    depth, score = 0, 0
    for i in b:
        if i == '{':
            depth += 1
            score += depth
        if i == '}':
            depth -= 1

    return score


def part_2(data):
    a = re.sub(r'!\S', '', data)  # Remove '!' and cancelled
    c = re.findall(r'<([^>]*)>', a)  # Find all garbage

    return sum(len(i) for i in c)


with open("day_09_input.txt") as f:
    inp = f.readlines()[0]
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))