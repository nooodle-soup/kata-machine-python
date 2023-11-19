from src.katas.BinarySearch import binary_search
import pytest 


@pytest.mark.parametrize(
    "haystack, needle",
    [
        ([1, 2, 3, 4, 5], 5),
    ]
)
def test_binary_search_pass(haystack, needle):
    assert binary_search(haystack, needle)


@pytest.mark.parametrize(
    "haystack, needle",
    [
        ([1, 2, 3, 4, 5], 6),
    ]
)
def test_binary_search_fail(haystack, needle):
    assert not binary_search(haystack, needle)
