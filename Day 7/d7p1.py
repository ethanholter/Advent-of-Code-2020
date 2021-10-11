# Day 7 Part 1

# How many bag colors can eventually contain at least one shiny gold bag? 
# (The list of rules is quite long; make sure you get all of it.)

# step 1: find each bag which can contain a "shiny gold bag"
# step 2: for each of those bags, find which bags can contain it
# step 3: repeat recursivly until no more bags can be found

import re

input = open(r"Day 7\input.txt", "r").read().split("\n")

def addNewBags(oldBags, newBags):
    for bag in newBags:
        if bag in oldBags:
            continue
        else:
            oldBags.append(bag)
    return oldBags


def solve(input, parentBags):
    numCombos = 0
    totalBags = []
    bags = []
    while len(parentBags) > 0:
        bags = []
        for rule in input:
            rule = re.sub(" contain|\d|[,.]","",rule).split('  ')
            for i in range(1, len(rule)):
                if any(bag in rule[i] for bag in parentBags):
                    numCombos += 1
                    bags.append(rule[0].rstrip(' bags'))
        parentBags = bags
        totalBags = addNewBags(totalBags, parentBags)
    # return {"bags":parentBags, "combinations": numCombos}
    return totalBags.__len__()

print(solve(input, ["shiny gold"]))