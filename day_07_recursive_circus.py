import re


node_map = {}
node_values = {}


def solve(data, *, part):
    for line in data:
        name, weight, *children = re.findall(r'\w+', line)
        node_values[name] = int(weight)
        if children:
            node_map[name] = children

    nodes = node_map.keys()
    nodes_w_children = [i for v in node_map.values() for i in v]
    root = list(set(nodes) - set(nodes_w_children))[0]

    if part == 1:
        return root
    if part == 2:
        return sum_descendants(root)


def sum_descendants(node):
    children = node_map[node]
    arm_totals = {}
    for child in children:
        value = node_values[child]
        if child in node_map.keys():
            value += sum(sum_descendants(child).values())
        arm_totals[child] = value
    if len(set(arm_totals.values())) != 1:
        k = list(arm_totals.keys())
        v = list(arm_totals.values())
        unbalanced_total = min(v, key=v.count)
        balanced_total = max(v, key=v.count)
        unbalanced_value = node_values[k[v.index(unbalanced_total)]]

        print(unbalanced_value - (unbalanced_total - balanced_total))
        exit()  # I don't like this either but I'm too burnt out to change it.
    return arm_totals


if __name__ == '__main__':
    with open("day_07_input.txt") as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(solve(inp, part=1)))
        print("Part 2 answer: ", end="")
        solve(inp, part=2)
