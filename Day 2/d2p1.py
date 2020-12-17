#Day 1 Part 1

# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number 
# of times a given letter must appear for the password to be 
# valid. For example, 1-3 a means that the password must 
# contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, 
# cdefg, is not; it contains no instances of b, but needs at least 1. 
# The first and third passwords are valid: they contain one a or nine c, 
# both within the limits of their respective policies.

# How many passwords are valid according to their policies?
import re

input = open(r"Day 2\input.txt", "r").read().split("\n")

def numChars(char, input):
    count = 0
    for item in list(input):
        if item == char:
            count += 1
    return count

def solve(input):
    correctPasswords = 0
    for item in input:
        item = re.findall(r"[\w']+", item) #[min, max, char, password]
        letterCount = numChars(item[2], item[3])
        if letterCount >= int(item[0]) and letterCount <= int(item[1]):
            correctPasswords += 1
    return correctPasswords

print(solve(input))
