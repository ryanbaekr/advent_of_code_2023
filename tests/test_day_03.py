"""Testing for Day 03"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_03")

def test_sums() -> None:
    """Test gear_ratios"""

    with open(FIXTURE, encoding="utf-8") as f:
        schematic = f.read()

    part_sum, gear_sum = aoc.gear_ratios(schematic)

    assert part_sum == 546563
    assert gear_sum == 91031374
