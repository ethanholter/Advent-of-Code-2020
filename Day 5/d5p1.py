#Day 5 Part 1

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

# input = ["BFFFBBFRRR"]

input = open(r"Day 5\input.txt", "r").read().split("\n")


def convertToBinary(input, zeroVal, oneVal, stripChars):
    input = input.strip(stripChars)
    input = input.replace(zeroVal, "0")
    input = input.replace(oneVal, "1")
    return int(input, 2)

def solve(input):
    largestID = 0
    largestSeat = ""
    for seat in input:
        row = convertToBinary(seat, "F", "B", "RL")
        col = convertToBinary(seat, "L", "R", "FB")
        seatID = row * 8 + col
        if seatID > largestID:
            largestID = seatID
            largestSeat = seat
    return {"ID": largestID, "Name": largestSeat}


print(solve(input))