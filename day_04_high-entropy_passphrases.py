def part_1(data):
    phrases = [phrase.split() for phrase in data]
    return sum(sorted(p) == sorted(list(set(p))) for p in phrases)


def part_2(data):
    phrases = [phrase.split() for phrase in data]
    phrases = [["".join(sorted(word)) for word in phrase] for phrase in phrases]
    return sum(sorted(p) == sorted(list(set(p))) for p in phrases)


with open("day_04_input.txt") as f:
    inp = f.readlines()
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))
