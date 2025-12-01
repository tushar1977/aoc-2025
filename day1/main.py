with open("t.txt", "r") as f:
    parts = f.read().strip().split("\n")
# ans = 289042678603
ans = 50
rnt = 0
for i in parts:
    side = i[0]
    dis = int(i[1:])

    if side == "L":
        for i in range(dis, 0, -1):
            ans -= 1
            ans %= 100
            if ans == 0:
                rnt += 1
    else:
        for i in range(dis, 0, -1):
            ans += 1
            ans %= 100
            if ans == 0:
                rnt += 1


print(rnt)
