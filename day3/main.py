with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n")
ans = 0


def part2(parts):
    ans = 0
    for line in parts:
        nums = [*map(int, line)]
        n = 0

        for i in range(11, -1, -1):
            temp = nums[: len(nums) - i]
            maxi = max(temp)
            idx = temp.index(maxi)
            nums = nums[idx + 1 :]
            n = n * 10 + maxi
        ans += n
    print(ans)


def part1(parts):
    ans = 0

    for bank in parts:
        bank = str(bank)
        n = len(bank)
        best_digit = bank[0]

        dp = [0] * n

        for i in range(1, n):
            pair_val = int(best_digit + bank[i])
            dp[i] = max(dp[i - 1], pair_val)

            if best_digit < bank[i]:
                best_digit = bank[i]

        ans += dp[n - 1]

    print(ans)


part1(parts)
part2(parts)
