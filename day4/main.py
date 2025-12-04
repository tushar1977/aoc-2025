with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]


directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

n = len(grid)
m = len(grid[0])


def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < n)


def part1(grid):
    to_replace = []
    for i in range(0, n):
        for j in range(0, m):
            if grid[i][j] == "@":
                cnt = 0
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if in_grid(ni, nj) and grid[ni][nj] == "@":
                        cnt += 1
                if cnt < 4:
                    to_replace.append((i, j))
    for i, j in to_replace:
        grid[i][j] = "."

    return len(to_replace)


def part2(grid, last_ans):
    final_ans = 0

    while last_ans != 0:
        final_ans += last_ans
        last_ans = part1(grid)

    return final_ans


a1 = part1(grid)
a2 = part2(grid, a1)

print(a1)
print(a2)
