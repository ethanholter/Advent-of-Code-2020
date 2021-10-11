# Day 7 Part 2


import re

input = open(r"Day 7\input.txt", "r").read().split("\n")

# input = """shiny gold bags contain 2 dark red bags, 2 crazy purple bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# crazy purple bags contain no other bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.""".split("\n")

# input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3x faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.""".split("\n")

ParentBags = ["shiny gold"]
parentBagNums = [1]
foundBag = True

def containsField(str, arr):
    for item in arr:
        if str.__contains__(item): return item
    return False

for rule in input:
    newRule = re.sub(" bags contain no other bags.", "", rule)
    newRule = re.sub(" contain|[,]", "#", newRule).split("#")
    for i in range(len(newRule)):
        newRule[i] = re.sub("[,.]|^\s| bags| bag", "", newRule[i])
    input[input.index(rule)] = newRule

totalBags = 0
while foundBag:
    foundBag = False
    newParentBags = []
    newParentBagNums = []
    for rule in input:
        parent = containsField(rule[0], ParentBags)
        if parent != False:
            print(rule) 
        for i in range(1, len(rule)):
            num = int(re.sub("[^\d]", "", rule[i]))
            if parent != False:
                newParentBags.append(re.sub("[\d]", "", rule[i]).lstrip(" "))
                lineTotal = num * parentBagNums[ParentBags.index(parent)]
                newParentBagNums.append(lineTotal)
                # print("(%s) %s ----> %s - line total: %s" % (parentBagNums[ParentBags.index(parent)], parent, rule[i], lineTotal))
                totalBags += lineTotal
                foundBag = True
        if len(rule) == 1 and parent != False:
            lineTotal = parentBagNums[ParentBags.index(parent)]
            # print("(%s) %s ----> none" % (parentBagNums[ParentBags.index(parent)], parent))
                
    # print(newParentBags)
    print("total: %s" % totalBags)
    print("\n")
    parentBagNums = newParentBagNums
    ParentBags = newParentBags
print(totalBags)
