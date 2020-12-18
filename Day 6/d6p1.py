#Day 6 Part 1

# For each group, count the number of questions to which ANYONE answered "yes". What is the sum of those counts?

import re

input = open(r"Day 6\input.txt", "r").read().split("\n\n")

def solve(input):
    total = 0
    for group in input:
        group = group.split("\n")
        combinedAns = group[0]
        for form in group:
            newChars = re.sub("[\s%s]" %combinedAns, "", form)
            combinedAns = "".join((newChars, combinedAns))
        total += len(combinedAns)
    return total

print(solve(input))