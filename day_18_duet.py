from collections import defaultdict
import queue


def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False


def part_1(data):
    registers = defaultdict(int)
    last_sound = 0
    i = 0
    while True:
        inst, x, y = (data[i].split() + [None] * 3)[:3]
        val_1 = int(x) if is_int(x) else registers[x]
        if y is not None:
            val_2 = int(y) if is_int(y) else registers[y]

        if inst == 'snd':
            last_sound = val_1
        if inst == 'set':
            registers[x] = val_2
        if inst == 'add':
            registers[x] += val_2
        if inst == 'mul':
            registers[x] *= val_2
        if inst == 'mod':
            registers[x] %= val_2
        if inst == 'jgz':
            if val_1 > 0:
                i += val_2
                continue
        if inst == 'rcv':
            if val_1 != 0:
                return last_sound
        i += 1


def part_2(data):
    registerses = [defaultdict(int, p=0), defaultdict(int, p=1)]
    queues = [queue.Queue(), queue.Queue()]
    indices = [0, 0]
    waiting = [False, False]
    count = 0
    while True:
        for p_id in range(2):
            registers = registerses[p_id]

            inst, x, y = (data[indices[p_id]].split() + [None] * 3)[:3]
            val_1 = int(x) if is_int(x) else registers[x]
            if y is not None:
                val_2 = int(y) if is_int(y) else registers[y]

            if inst == 'snd':
                queues[(p_id+1) % 2].put(val_1)
                count += (p_id == 1)
            if inst == 'set':
                registers[x] = val_2
            if inst == 'add':
                registers[x] += val_2
            if inst == 'mul':
                registers[x] *= val_2
            if inst == 'mod':
                registers[x] %= val_2
            if inst == 'jgz':
                if val_1 > 0:
                    indices[p_id] += val_2
                    continue
            if inst == 'rcv':
                if queues[p_id].empty():
                    if waiting[(p_id+1) % 2]:
                        return count
                    waiting[p_id] = True
                    continue
                else:
                    waiting[p_id] = False
                    registers[x] = queues[p_id].get()
            indices[p_id] += 1


if __name__ == '__main__':
    with open('day_18_input.txt') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
