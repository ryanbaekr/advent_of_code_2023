"""Testing for Day 05"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_05")

def test_as_value() -> None:
    """Test if_you_give_a_seed_a_fertilizer with as_range=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        almanac = f.read()

    location = aoc.if_you_give_a_seed_a_fertilizer(almanac, as_range=False)

    assert location == 107430936


def test_as_range() -> None:
    """Test if_you_give_a_seed_a_fertilizer with as_range=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        almanac = f.read()

    location = aoc.if_you_give_a_seed_a_fertilizer(almanac, as_range=True)

    assert location == 23738616
