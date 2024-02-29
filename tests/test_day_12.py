"""Testing for Day 12"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_12")

def test_unfolded() -> None:
    """Test hot_springs with folded=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        records = f.read()

    arrangements = aoc.hot_springs(records, folded=False)

    assert arrangements == 7260


def test_folded() -> None:
    """Test hot_springs with folded=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        records = f.read()

    arrangements = aoc.hot_springs(records, folded=True)

    assert arrangements == 1909291258644
