from itertools import permutations


def calculate_checksum(data, *, part):
    rows = [list(map(int, row.split())) for row in data]
    if part == 1:
        return sum(max(nums) - min(nums) for nums in rows)
    else:
        return sum(i // j for nums in rows
                   for i, j in permutations(nums, r=2)
                   if i % j == 0)


if __name__ == '__main__':
    with open("day_02_input.txt") as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(calculate_checksum(inp, part=1)))
        print("Part 2 answer: " + str(calculate_checksum(inp, part=2)))
