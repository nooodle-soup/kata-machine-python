"""
Highest Value Plot

A land owner is trying to sell a plot of land from his series of plots. He
wants to find the highest valued plot. You can think of a plot as two adjacent
cells in the array. The value of each plot can be calulated by multiplying the
cost of each adjacent cell.
"""


def highestValuePlotFinder(costs):
    """
    Parameters
    ----------
    costs: list of int
        The cost of each ith cell of land

    Returns
    -------
    int:
        The highest value of a plot from all possible plots
    """

    result = costs[0] * costs[1]

    for i in range(1, len(costs) - 1):
        result = max(result, costs[i] * costs[i+1])

    return result
