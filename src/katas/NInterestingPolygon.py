"""
Area of n-Interesting Polygon

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim, side by side. You can see the
1-, 2-, 3- and 4-interesting polygons in the picture below.

                             --
  1-interesting polygon --> |  |
                             --

                                --
                               |  |
                             -- -- --
  2-interesting polygon --> |  |  |  |
                             -- -- --
                               |  |
                                --

                                   --
                                  |  |
                                -- -- --
                               |  |  |  |
                             -- -- -- -- --
  3-interesting polygon --> |  |  |  |  |  |
                             -- -- -- -- --
                               |  |  |  |
                                -- -- --
                                  |  |
                                   --

                                      --
                                     |  |
                                   -- -- --
                                  |  |  |  |
                                -- -- -- -- --
                               |  |  |  |  |  |
                             -- -- -- -- -- -- --
  4-interesting polygon --> |  |  |  |  |  |  |  |
                             -- -- -- -- -- -- --
                               |  |  |  |  |  |
                                -- -- -- -- --
                                  |  |  |  |
                                   -- -- --
                                     |  |
                                      --

"""


def nInterestingPolygonAreaFinder(n):
    """
    Parameters
    ----------
    n: int
        The number which describes the n-interesting polygon.

    Returns
    -------
    int:
        Area of the n-interesting polygon.
    """

    base = 2*n - 1
    area = base

    next_step = base - 2

    while next_step >= 1:
        area += 2*next_step
        next_step -= 2

    # return n**2 + (n-1)**2
    return area

