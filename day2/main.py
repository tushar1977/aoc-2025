with open("t.txt", "r") as f:
    parts = f.read().strip().split(",")


def part2(a, b):
    ans = 0
    for j in range(a, b + 1):
        s = str(j)
        for x in range(1, len(s)):
            sub = s[:x]
            if sub * (len(s) // len(sub)) == s:
                ans += int(s)
    return ans


def part1():
    ans = 0
    total = 0
    for i in parts:
        a, b = i.split("-")
        a = int(a)
        b = int(b)

        total += part2(a, b)

        for j in range(a, b + 1):
            s = str(j)
            if len(s) % 2 != 0:
                continue
            mid = len(s) // 2
            first_half = s[:mid]
            if first_half * 2 == s:
                ans += j

    print(ans)
    print(total)


part1()
