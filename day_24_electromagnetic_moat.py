from collections import defaultdict


def part_1(data):
    ports = defaultdict(set)
    for line in data:
        a, b = [int(i) for i in line.split('/')]
        ports[a].add(b)
        ports[b].add(a)

    bridges = list(get_bridges(ports, [(0, 0)]))
    return max(sum(x + y for x, y in bridge) for bridge in bridges)


def part_2(data):
    ports = defaultdict(set)
    for line in data:
        a, b = [int(i) for i in line.split('/')]
        ports[a].add(b)
        ports[b].add(a)

    bridges = list(get_bridges(ports, [(0, 0)]))
    bridges.sort(key=lambda bridge: sum(x + y for x, y in bridge))
    bridges.sort(key=len)

    return sum(a + b for a, b in bridges[-1])


def get_bridges(ports, bridge):
    pins_1 = bridge[-1][1]

    for pins_2 in ports[pins_1]:
        if not((pins_1, pins_2) in bridge or (pins_2, pins_1) in bridge):
            new_bridge = bridge + [(pins_1, pins_2)]
            yield new_bridge
            yield from get_bridges(ports, new_bridge)


if __name__ == '__main__':
    with open('day_24_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
