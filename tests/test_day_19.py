"""Testing for Day 19"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_19")

def test_sums() -> None:
    """Test aplenty"""

    with open(FIXTURE, encoding="utf-8") as f:
        workflows = f.read()

    accepted, distinct = aoc.aplenty(workflows)

    assert accepted == 325952
    assert distinct == 125744206494820
