"""Testing for Day 17"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_17")

def test_normal() -> None:
    """Test clumsy_crucible with ultra=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        city_map = f.read()

    loss = aoc.clumsy_crucible(city_map, ultra=False)

    assert loss == 1023


def test_ultra() -> None:
    """Test clumsy_crucible with ultra=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        city_map = f.read()

    loss = aoc.clumsy_crucible(city_map, ultra=True)

    assert loss == 1165
