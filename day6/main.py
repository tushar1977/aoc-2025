with open("t.txt", "r") as f:
    lines = [line.strip("\n") for line in f]

grid = [row.split() for row in lines]
problems = list(zip(*grid))
print(problems)


def part1():
    ans = 0
    for problem in problems:
        *nums, op = problem
        nums = list(map(int, nums))
        result = 0

        if op == "+":
            result = sum(nums)
        elif op == "*":
            result = 1
            for n in nums:
                result *= n
        ans += result
    print(ans)


def part2():
    total = 0

    rotated = list(zip(*problems))[::-1]

    for col in rotated:
        *nums, op = col

        built_numbers = []
        for num in nums:
            if num.strip():
                built_numbers.append(int(num[::-1]))

        if op == "+":
            result = sum(built_numbers)
        else:
            result = 1
            for n in built_numbers:
                result *= n

        total += result

    print(total)


part2()
