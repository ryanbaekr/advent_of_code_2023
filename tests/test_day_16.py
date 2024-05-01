"""Testing for Day 16"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_16")

def test_sum() -> None:
    """Test the_floor_will_be_lava with best=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        layout = f.read()

    tiles = aoc.the_floor_will_be_lava(layout, best=False)

    assert tiles == 6902


def test_best() -> None:
    """Test the_floor_will_be_lava with best=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        layout = f.read()

    tiles = aoc.the_floor_will_be_lava(layout, best=True)

    assert tiles == 7697
