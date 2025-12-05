with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n")

ranges = []


def part1(parts):
    ans = 0
    queries = []
    for p in parts:
        if p != "":
            if "-" in p:
                l, r = map(int, p.split("-"))
                ranges.append((l, r))
            else:
                queries.append(int(p))

    for q in queries:
        for l, r in ranges:
            if l <= q <= r:
                ans += 1
                break
    return ans


print(part1(parts))

for p in parts:
    l, r = map(int, p.split("-"))
    ranges.append((l, r))

ranges.sort()
ans = 0
merged = []

for l, r in ranges:
    if not merged or l > merged[-1][1] + 1:
        merged.append([l, r])
    else:
        merged[-1][1] = max(merged[-1][1], r)

for l, r in merged:
    ans += r - l + 1

print(ans)
