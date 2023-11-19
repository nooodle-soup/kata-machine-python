from src.katas.BandwidthDistribution import distributeBandwidth
import pytest


@pytest.mark.parametrize(
    "bandwidths, requests, total_bandwidth, expected_result",
    [
        (
            [200, 100, 350, 50, 100],
            [270, 142, 450, 124, 189],
            500,
            763
        )
    ]
)
def test_BandwidthDistribution(bandwidths, requests, total_bandwidth, expected_result):
    assert distributeBandwidth(
        bandwidths, requests, total_bandwidth
    ) == expected_result
