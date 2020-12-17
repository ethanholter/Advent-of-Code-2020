#Day 2
# What is the product of the three entries that sum to 2020?

input = open(r"Day 1\input.txt", "r").read().split("\n")
for item in input:
    input[input.index(item)] = int(item)
    
def solve(input):
    for item1 in input:
        for item2 in input:
            for item3 in input:
                if item2 is item1 or item2 is item3 or item1 is item3:
                    continue
                else:
                    if item1 + item2 + item3 == 2020:
                        return item1 * item2 * item3
                    
print(solve(input))