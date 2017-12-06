def count_valid(data, *, part):
    phrases = [phrase.split() for phrase in data]
    if part == 2:
        phrases = [["".join(sorted(word)) for word in phrase] for phrase in phrases]
    return sum(sorted(p) == sorted(list(set(p))) for p in phrases)


if __name__ == '__main__':
    with open("day_04_input.txt") as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(count_valid(inp, part=1)))
        print("Part 2 answer: " + str(count_valid(inp, part=2)))