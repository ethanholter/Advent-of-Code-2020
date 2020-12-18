#Day 5 Part 2

#Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#What is the ID of your seat?


input = open(r"Day 5\input.txt", "r").read().split("\n")

def convertToBinary(input, zeroVal, oneVal, stripChars):
    input = input.strip(stripChars)
    input = input.replace(zeroVal, "0")
    input = input.replace(oneVal, "1")
    return int(input, 2)

def solve(input):
    allSeats = []
    for seat in input:
        row = convertToBinary(seat, "F", "B", "RL")
        col = convertToBinary(seat, "L", "R", "FB")
        seatID = row * 8 + col
        allSeats.append(seatID)

    allSeats = sorted(allSeats)
    for i in range(1, len(allSeats)):
        if allSeats[i] != allSeats[i-1] + 1:
            return allSeats[i] - 1

print(solve(input))