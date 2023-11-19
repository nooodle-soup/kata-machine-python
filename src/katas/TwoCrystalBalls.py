from math import floor, sqrt


def two_crystal_balls(breaks: list[bool]) -> int:
    jumpAmt = floor(sqrt(len(breaks)))
    i = 0

    for i in range(0, len(breaks), jumpAmt):
        if breaks[i]:
            break

    i -= jumpAmt

    for j in range(i, len(breaks)):
        if breaks[j]:
            return j

    return -1
