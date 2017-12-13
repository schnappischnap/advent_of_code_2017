from functools import reduce
from operator import xor


def part_1(data):
    nums = list(range(256))
    keys = [int(c) for c in data.split(",")]
    pos, skip = 0, 0

    for length in keys:
        reverse_slice(nums, pos, length)
        pos = (pos + length + skip) % len(nums)
        skip += 1

    return nums[0] * nums[1]


def part_2(data):
    nums = list(range(256))
    keys = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    pos, skip = 0, 0

    for _ in range(64):
        for length in keys:
            reverse_slice(nums, pos, length)
            pos = (pos + length + skip) % len(nums)
            skip += 1

    dense = [reduce(xor, nums[i:i + 16]) for i in range(0, 256, 16)]
    return "".join(format(i, '02x') for i in dense)


def reverse_slice(a, start, length):
    if length > len(a) or length == 0:
        return

    sliced = list(reversed((a*2)[start:start+length]))
    for i in range(length):
        a[(start+i) % len(a)] = sliced[i]


with open("day_10_input.txt") as f:
    inp = f.readlines()[0]
    print("Part 1 answer: " + str(part_1(inp)))
    print("Part 2 answer: " + str(part_2(inp)))
