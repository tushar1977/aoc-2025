with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]

n = len(grid)
m = len(grid[0])

rows = n
cols = m
dp = [[-1 for _ in range(cols)] for _ in range(rows)]

def isValid(r, c):
    if r < n and r >= 0 and c < m and c >= 0:
        return True
    return False

def part1(i, j):
    l = [(i, j)]
    ans = 0
    visited = set()

    while l:
        i, j = l.pop()

        if not isValid(i, j):
            continue
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if grid[i][j] == "^":
            ans += 1

            l.append((i, j - 1))
            l.append((i, j + 1))
        else:
            l.append((i + 1, j))
    return ans

def part2(i, j):
    if i == n: return 1
    if not isValid(i, j): return 0
    if dp[i][j] != -1: return dp[i][j]

    if grid[i][j] == "^":
        dp[i][j] = part2(i + 1, j - 1) + part2(i + 1, j + 1)
    else:
        dp[i][j] = part2(i + 1, j)
    return dp[i][j]

ans2 = 0
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            ans = part1(i, j)
            ans2 = part2(i, j)
            break
print(ans)
print(ans2)
