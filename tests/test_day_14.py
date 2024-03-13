"""Testing for Day 14"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_14")

def test_single() -> None:
    """Test parabolic_reflector_dish with spin=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        positions = f.read()

    load = aoc.parabolic_reflector_dish(positions, spin=False)

    assert load == 110274


def test_spin() -> None:
    """Test parabolic_reflector_dish with spin=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        positions = f.read()

    load = aoc.parabolic_reflector_dish(positions, spin=True)

    assert load == 90982
