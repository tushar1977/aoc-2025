with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]

n = len(grid)
m = len(grid[0])
dp = [[-1 for _ in range(m)] for _ in range(n)]
def isValid(r, c):
    return 0 <= r < n and 0 <= c < m

visited = set()
def part1(i, j):
    ans = 0
    if not isValid(i, j): return 0
    if (i,j) in visited: return 0

    visited.add((i,j))

    if(grid[i][j] == '^'):
        ans += 1
        ans += part1(i, j-1)
        ans += part1(i, j+1)
    else:
        ans += part1(i+1, j)
    return ans

visited_p2 = set()
def part2(i, j):
    if i == n: return 1
    visited_p2.add((i,j))
    if not isValid(i, j): return 0
    if dp[i][j] != -1: return dp[i][j]


    if grid[i][j] == "^":
        dp[i][j] = part2(i + 1, j - 1) + part2(i + 1, j + 1)
    else:
        dp[i][j] = part2(i + 1, j)
    return dp[i][j]


ans = 0
ans2 = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            ans = part1(i, j)
            ans2 = part2(i, j)
            break

print(ans)
print(ans2)
