from itertools import permutations


def part_1(data):
    rows = [list(map(int, row.split())) for row in data]
    return sum(max(nums) - min(nums) for nums in rows)


def part_2(data):
    rows = [list(map(int, row.split())) for row in data]
    return sum(i // j for nums in rows
               for i, j in permutations(nums, r=2)
               if i % j == 0)


if __name__ == '__main__':
    with open('day_02_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
