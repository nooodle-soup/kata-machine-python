"""
Two Crystal Balls

You possess two crystal balls, both of which are designed to break upon impact
when thrown from a building. Your challenge is to determine the lowest floor
from which the crystal balls will shatter upon landing.

Strategically use these crystal balls to pinpoint the exact floor where their
fragility is revealed.
"""


from math import floor, sqrt


def two_crystal_balls(breaks: list[bool]) -> int:
    """
    Parameters
    ----------
    breaks: list[bool]
        A boolean list if the ball breaks on the ith floor.

    Returns
    -------
    int:
        The first floor at which the ball breaks.
    """
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
