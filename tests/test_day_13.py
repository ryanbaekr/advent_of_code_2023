"""Testing for Day 13"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_13")

def test_clear() -> None:
    """Test point_of_incidence with smudges=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        patterns = f.read()

    summary = aoc.point_of_incidence(patterns, smudges=False)

    assert summary == 40006


def test_smudge() -> None:
    """Test point_of_incidence with smudges=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        patterns = f.read()

    summary = aoc.point_of_incidence(patterns, smudges=True)

    assert summary == 28627
