from katas.HighestValuePlot import highestValuePlotFinder
import pytest


@pytest.mark.parametrize(
    "costs, expected_result",
    [
        ([3, 6, -2, -5, 7, 3], 21),
        ([3, 6], 18),
    ]
)
def test_highestValuePlotFinder(costs, expected_result):
    assert highestValuePlotFinder(costs) == expected_result
