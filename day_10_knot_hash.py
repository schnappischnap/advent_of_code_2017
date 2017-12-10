from functools import reduce
from operator import xor


def solve_hash(data, *, part):
    nums = list(range(256))
    if part == 1:
        keys = [int(c) for c in data.split(",")]
    else:
        keys = [ord(c) for c in data] + [17, 31, 73, 47, 23]

    pos, skip = 0, 0
    cycles = 1 if part == 1 else 64

    for _ in range(cycles):
        for length in keys:
            reverse_slice(nums, pos, length)
            pos = (pos + length + skip) % len(nums)
            skip += 1

    if part == 1:
        return nums[0] * nums[1]

    dense = [reduce(xor, nums[i:i+16]) for i in range(0, 256, 16)]
    return "".join(format(i, '02x') for i in dense)


def reverse_slice(a, start, length):
    if length > len(a) or length == 0:
        return

    sliced = list(reversed((a*2)[start:start+length]))
    for i in range(length):
        a[(start+i) % len(a)] = sliced[i]


if __name__ == '__main__':
    with open("day_10_input.txt") as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(solve_hash(inp, part=1)))
        print("Part 2 answer: " + str(solve_hash(inp, part=2)))
