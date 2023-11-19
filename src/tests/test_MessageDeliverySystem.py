from src.katas.MessageDeliverySystem import getMessageStatus
import pytest


@pytest.mark.parametrize(
    "timestamps, messages, k, expected_result",
    [
        (
            [1, 4, 5, 10, 11, 14],
            ["Hello", "Bye", "Bye", "Hello", "Bye", "Hello"],
            5,
            [True, True, False, True, True, False]
        ),
    ]
)
def test_MessageDeliverySystem(timestamps, messages, k, expected_result):
    assert getMessageStatus(
        timestamps,
        messages,
        k
    ) == expected_result
