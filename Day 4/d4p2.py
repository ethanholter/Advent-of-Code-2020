#Day 4 Part 2

#Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

#true inputs
# input = ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"]
# input = ["eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"]
# input = ["hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022"]

#false inputs
# input = ["hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"]
# input = ["hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"]

import re

input = open(r"Day 4\input.txt", "r").read().split("\n\n")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def numBetween(min, max, input):
    input = int(input)
    return input >= min and input <= max

def containsFields(str, arr):
    for item in arr:
        if not str.__contains__(item): return False
    return True

def passportCorrect(passport):
    passport = re.findall(r"[^:\s]+", passport)
    for i in range(len(passport)//2):
        i *= 2
        if not fitsFieldCriteria(passport[i], passport[i+1]): return False
    return True


def fitsFieldCriteria(field, str):
    if field == "byr":
        if numBetween(1920, 2002, str): return True
    elif field == "iyr":
        if numBetween(2010, 2020, str): return True
    elif field == "eyr":
        if numBetween(2020, 2030, str): return True
    elif field == "hgt":
        if str.__contains__("in"):
            str = str.replace("in", "")
            if numBetween(59, 76, str): return True
        if str.__contains__("cm"):
            str = str.replace("cm", "")
            if numBetween(150, 193, str): return True
    elif field == "hcl":
        return re.search("[^#0123456789abcdef]", str) == None and str.startswith("#")
    elif field == "ecl":
        if re.findall("amb|blu|brn|gry|grn|hzl|oth", str) and len(str) == 3: return True
    elif field == "pid":
        return len(str) == 9 and not re.findall("[^0-9]", str)
    elif field == "cid": return True
    return False

def solve(input, fields):
    correctPassports = 0
    for passport in input:
        if containsFields(passport, fields) and passportCorrect(passport):
            correctPassports += 1
    return correctPassports

print(solve(input, requiredFields))

