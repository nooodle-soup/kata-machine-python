from src.katas.TwoCrystalBalls import two_crystal_balls
import pytest


def test_two_crystal_balls():
    assert (
        two_crystal_balls(
            [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                True,
                True,
                True,
                True,
                True,
            ]
        )
        == 10
    )
