#Day 3 Part 2

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
#What do you get if you multiply together the number of trees encountered on each of the listed slopes?

input = open(r"Day 3\input.txt", "r").read().split("\n")

tree = '#'
empty = '.'
patterns = [
{"right": 1, "down": 1},
{"right": 3, "down": 1},
{"right": 5, "down": 1},
{"right": 7, "down": 1},
{"right": 1, "down": 2}]


for item in input:
    input[input.index(item)] = list(item)

def solve(input, pattern):
    treeCounter = 0
    x = 0
    y = 0
    while y < len(input):
        #print(input[y][x])
        if input[y][x] == tree:
            treeCounter += 1
        if x >= len(input[0]) - pattern["right"]:
            x -= 31
        x += pattern["right"]
        y += pattern["down"]
    return treeCounter

total = 1

for pattern in patterns:
    output = solve(input, pattern)
    print(output)
    total *= output

print(total)