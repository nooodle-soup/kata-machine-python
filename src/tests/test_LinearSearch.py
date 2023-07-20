from src.katas.LinearSearch import linear_search
import pytest


@pytest.mark.linear_search
@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ([1, 2, 3, 4, 5], 5, True),
        ([1, 2, 3, 4, 5], 4, True),
        ([1, 2, 3, 4, 5], 3, True),
    ],
)
def test_linear_search(haystack, needle, expected):
    assert linear_search(haystack, needle) is expected
