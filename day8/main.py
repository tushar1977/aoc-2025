import math

with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n")

coords = []

for i in parts:
    x, y, z = i.split(",")
    coords.append((int(x), int(y), int(z)))

dis = []
junctions = {}

n = len(coords)


def find_dis(x1, y1, z1, x2, y2, z2):
    p1 = math.pow(abs(x1 - x2), 2)
    p2 = math.pow(abs(y1 - y2), 2)
    p3 = math.pow(abs(z1 - z2), 2)

    return math.sqrt(p1 + p2 + p3)


for i in range(0, n):
    for j in range(i + 1, n):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dis.append((find_dis(x1, y1, z1, x2, y2, z2), i, j))
dis.sort()


def part1():
    s2 = [{i} for i in range(n)]
    cnt = 1
    for _, idx_i, idx_j in dis:
        if cnt > 1000:
            break
        set_a = None
        set_b = None

        for grp in s2:
            if idx_i in grp:
                set_a = grp
            if idx_j in grp:
                set_b = grp

        if set_a is not None and set_b is not None and set_a is not set_b:
            merged = set_a | set_b
            s2.remove(set_a)
            s2.remove(set_b)
            s2.append(merged)
        cnt += 1
    l = []
    for i in s2:
        if len(i) not in l:
            l.append(len(i))
    l.sort()
    return l[-1] * l[-2] * l[-3]


def part2():
    s2 = [{i} for i in range(n)]
    last_i = 0
    last_j = 0

    for _, idx_i, idx_j in dis:
        set_a = None
        set_b = None

        for grp in s2:
            if idx_i in grp:
                set_a = grp
            if idx_j in grp:
                set_b = grp

        if set_a is not None and set_b is not None and set_a is not set_b:
            merged = set_a | set_b
            s2.remove(set_a)
            s2.remove(set_b)
            s2.append(merged)

            last_i = idx_i
            last_j = idx_j

            if len(s2) == 1:
                break

    return coords[last_i][0] * coords[last_j][0]


print(part1())
print(part2())
