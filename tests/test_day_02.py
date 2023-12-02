"""Testing for Day 02"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_02")

def test_sums() -> None:
    """Test cube_conundrum"""

    with open(FIXTURE, encoding="utf-8") as f:
        records = f.read()

    valid_sum, power_sum = aoc.cube_conundrum(records)

    assert valid_sum == 2716
    assert power_sum == 72227
