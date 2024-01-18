"""Testing for Day 09"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_09")

def test_forward() -> None:
    """Test mirage_maintenance with reverse=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        report = f.read()

    prediction = aoc.mirage_maintenance(report, reverse=False)

    assert prediction == 1916822650


def test_backward() -> None:
    """Test mirage_maintenance with reverse=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        report = f.read()

    prediction = aoc.mirage_maintenance(report, reverse=True)

    assert prediction == 966
