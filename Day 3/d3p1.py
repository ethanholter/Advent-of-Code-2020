#Day 3 Part 1

#Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees("#") would you encounter? (The pattern repeats to the right forever)

input = open(r"Day 3\input.txt", "r").read().split("\n")

tree = '#'
empty = '.'

for item in input:
    input[input.index(item)] = list(item)

def solve(input):
    treeCounter = 0
    x = 0
    y = 0
    while y < len(input):
        if input[y][x] == tree:
            treeCounter += 1
        if x >= len(input[0]) - 3:
            x -= 31
        x += 3
        y += 1
    return treeCounter

total = 1

print(solve(input))