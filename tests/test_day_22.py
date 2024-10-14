"""Testing for Day 22"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_22")

def test_sums() -> None:
    """Test sand_slabs"""

    with open(FIXTURE, encoding="utf-8") as f:
        snapshot = f.read()

    bricks, chain_sum = aoc.sand_slabs(snapshot)

    assert bricks == 451
    assert chain_sum == 66530
