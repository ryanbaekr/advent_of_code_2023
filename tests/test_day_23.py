"""Testing for Day 23"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_23")

def test_normal() -> None:
    """Test a_long_walk with traction=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        trails = f.read()

    steps = aoc.a_long_walk(trails, traction=False)

    assert steps == 2010


def test_traction() -> None:
    """Test a_long_walk with traction=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        trails = f.read()

    steps = aoc.a_long_walk(trails, traction=True)

    assert steps == 6318
