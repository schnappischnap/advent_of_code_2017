import re
from collections import defaultdict


def part_1(data):
    closest_distance = 1000000
    closest_particle = None
    for particle_id, line in enumerate(data):
        particle = tuple(map(int, re.findall(r'-?\d+', line)))
        pos, vel, acc = particle[:3], particle[3:6], particle[6:]

        pos2 = (calc_pos(pos[i], vel[i], acc[i], 1000) for i in range(3))

        distance = sum(abs(i) for i in pos2)
        if distance < closest_distance:
            closest_distance = distance
            closest_particle = particle_id

    return closest_particle


def part_2(data):
    particles = []
    for line in data:
        particle = tuple(map(int, re.findall(r'-?\d+', line)))
        particles.append((particle[:3], particle[3:6], particle[6:]))

    for t in range(1000):
        positions = defaultdict(list)

        for p in particles:
            pos, vel, acc = p
            pos2 = tuple(calc_pos(pos[i], vel[i], acc[i], t) for i in range(3))
            positions[pos2].append(p)

        dupes = [p for v in positions.values() for p in v if len(v) > 1]
        particles = [p for p in particles if p not in dupes]

    return len(particles)


def calc_pos(s, u, a, t):
    return s + t*(0.5*a*(t+1)+u)


if __name__ == '__main__':
    with open('day_20_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
