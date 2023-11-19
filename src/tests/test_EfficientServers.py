from src.katas.EfficientServers import efficientServerSetup
import pytest


@pytest.mark.parametrize(
    "memory, expected_result",
    [
        ([2, 1, 4, 3], 28)
    ]
)
def test_EfficientServers(memory, expected_result):
    assert efficientServerSetup(memory) == expected_result
