#Day 4 Part 1

#Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

input = open(r"Day 4\input.txt", "r").read().split("\n\n")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def containsFields(str, arr):
    for item in arr:
        if not str.__contains__(item): return False
    return True

def solve(input, fields):
    correctPassports = 0
    for item in input:
        if containsFields(item, fields):
            correctPassports += 1
    return correctPassports

print(solve(input, requiredFields))

