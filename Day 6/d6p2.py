#Day 6 Part 2

# For each group, count the number of questions to which EVERYONE answered "yes". What is the sum of those counts?

#for the record: part one took about an hour. part two took 30 seconds :)

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
        for form in group:
            combinedAns = re.sub("[^\s%s]" % form, "", combinedAns)
        total += len(combinedAns)
    return total

print(solve(input))