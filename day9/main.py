with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n")

coords = []

for i in parts:
    x, y = i.split(",")
    coords.append((int(x), int(y)))

n = len(coords)


def part1():
    ans = -10000000000000000
    for i in range(n):
        for j in range(n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            ans = max(ans, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    print(ans)


def part2():
    ans = -10000000000000000
    for i in range(n):
        for j in range(n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            size = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            if size > ans:
                ledgit = True

                for bb1 in range(n):
                    nexti = (bb1 + 1) % n
                    if not (
                        (
                            coords[bb1][1] >= max(coords[i][1], coords[j][1])
                            and coords[nexti][1] >= max(coords[i][1], coords[j][1])
                        )
                        or (
                            coords[bb1][1] <= min(coords[i][1], coords[j][1])
                            and coords[nexti][1] <= min(coords[i][1], coords[j][1])
                        )
                        or (
                            coords[bb1][0] <= min(coords[i][0], coords[j][0])
                            and coords[nexti][0] <= min(coords[i][0], coords[j][0])
                        )
                        or (
                            coords[bb1][0] >= max(coords[i][0], coords[j][0])
                            and coords[nexti][0] >= max(coords[i][0], coords[j][0])
                        )
                    ):
                        ledgit = False
                        break
                if ledgit:
                    ans = size

    print(ans)


part1()
part2()
