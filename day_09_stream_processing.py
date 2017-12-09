import re


def calculate_score(data):
    a = re.sub(r'!\S', '', data)     # Remove '!' and cancelled
    b = re.sub(r'<[^>]*>', '', a)    # Remove garbage
    c = re.findall(r'<([^>]*)>', a)  # Find all garbage

    depth, score = 0, 0
    for i in b:
        if i == '{':
            depth += 1
            score += depth
        if i == '}':
            depth -= 1

    return score, sum(len(i) for i in c)


if __name__ == '__main__':
    with open("day_09_input.txt") as f:
        inp = f.readlines()[0]
        out = calculate_score(inp)
        print("Part 1 answer: " + str(out[0]))
        print("Part 2 answer: " + str(out[1]))