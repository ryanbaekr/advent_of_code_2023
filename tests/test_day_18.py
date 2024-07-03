"""Testing for Day 18"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_18")

def test_normal() -> None:
    """Test lavaduct_lagoon with rgb=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        dig_plan = f.read()

    loss = aoc.lavaduct_lagoon(dig_plan, rgb=False)

    assert loss == 52055


def test_rgb() -> None:
    """Test lavaduct_lagoon with rgb=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        dig_plan = f.read()

    loss = aoc.lavaduct_lagoon(dig_plan, rgb=True)

    assert loss == 67622758357096
