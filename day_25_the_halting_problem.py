from collections import defaultdict


def part_1(data):
    state = data[0].strip()[-2]
    steps = int(data[1].strip().split()[-2])

    rules = {}
    for line in range(3, len(data), 10):
        s = data[line].strip()[-2]
        v_1 = int(data[line + 2].strip()[-2])
        m_1 = 1 if data[line + 3].strip().split()[-1] == 'right.' else -1
        s_1 = data[line + 4].strip()[-2]
        v_2 = int(data[line + 6].strip()[-2])
        m_2 = 1 if data[line + 7].strip().split()[-1] == 'right.' else -1
        s_2 = data[line + 8].strip()[-2]
        rules[s] = ((v_1, m_1, s_1), (v_2, m_2, s_2))

    tape = defaultdict(int)
    i = 0
    for _ in range(steps):
        if tape[i] == 0:
            tape[i] = rules[state][0][0]
            i += rules[state][0][1]
            state = rules[state][0][2]
        else:
            tape[i] = rules[state][1][0]
            i += rules[state][1][1]
            state = rules[state][1][2]

    return sum(i == 1 for i in tape.values())


if __name__ == '__main__':
    with open('day_25_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
