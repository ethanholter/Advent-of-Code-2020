#Day 2 Part 2

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

import re

input = open(r"Day 2\input.txt", "r").read().split("\n")

def solve(input):
    correctPasswords = 0
    for item in input:
        item = re.findall(r"[\w']+", item) #[pos1, pos2, char, password]
        passwordChars = list(item[3])
        if (passwordChars[int(item[0]) - 1] == item[2]) != (passwordChars[int(item[1]) - 1] == item[2]):
            correctPasswords += 1
    return correctPasswords

print(solve(input))