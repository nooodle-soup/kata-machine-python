from src.katas.BubbleSort import bubble_sort
import pytest 


@pytest.mark.parametrize(
    "bundle",
    [
        ([1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1]),
    ]
)
def test_bubble_sort(bundle):
    assert bubble_sort(bundle) == sorted(bundle)
