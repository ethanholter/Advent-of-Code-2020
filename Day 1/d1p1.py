#Day 1 part 1
#Find the two entries that sum to 2020; what do you get if you multiply them together?

input = open(r"Day 1\input.txt", "r").read().split("\n")
for item in input:
    input[input.index(item)] = int(item)

def solve(input):
    for item1 in input:
        for item2 in input:
            if item2 is item1:
                continue
            else:
                if item1 + item2 == 2020:
                    return item1 * item2
                    
print(solve(input))