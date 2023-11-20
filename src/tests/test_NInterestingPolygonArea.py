from katas.NInterestingPolygon import nInterestingPolygonAreaFinder
import pytest


@pytest.mark.parametrize(
    "n, expected_area",
    [
        (1, 1),
        (2, 5),
        (3, 13),
        (4, 25)
    ]
)
def test_nInterestingPolygonAreaFinder(n, expected_area):
    assert nInterestingPolygonAreaFinder(n) == expected_area
