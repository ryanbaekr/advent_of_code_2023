"""Testing for Day 04"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_04")

def test_sums() -> None:
    """Test scratchcards"""

    with open(FIXTURE, encoding="utf-8") as f:
        tickets = f.read()

    point_total, scrot_total = aoc.scratchcards(tickets)

    assert point_total == 28750
    assert scrot_total == 10212704
