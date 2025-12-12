from functools import cache

with open("t.txt") as f:
    lines = [line.strip() for line in f]

mp = {}

for p in lines:
    a, b = p.split(":")
    a = a.strip()
    val = b.strip().split()
    mp[a] = val


def part1():
    dst = "out"

    @cache
    def count_paths(src):
        if src == dst:
            return 1

        total = 0
        for nxt in mp.get(src, []):
            total += count_paths(nxt)

        return total

    print(count_paths("you"))


def part2():
    dst = "out"
    req = {"dac", "fft"}

    @cache
    def count_paths(src, found):
        if src in req:
            found = found | {src}
        if src == dst:
            return 1 if found == req else 0
        total = 0
        for nxt in mp.get(src, []):
            total += count_paths(nxt, found)
        return total

    print(count_paths("svr", frozenset()))


part1()
part2()
