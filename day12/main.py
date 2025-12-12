*shapes, regions = open("t.txt").read().split("\n\n")
shapes = [s.count("#") for s in shapes]
print(shapes)

answer = 0
for region in regions.strip().split("\n"):
    region, quants = region.split(": ")
    region = eval(region.replace("x", "*"))
    quants = eval(quants.replace(" ", ","))
    needed = sum(a * b for a, b in zip(quants, shapes))
    answer += needed < region

print(answer)
