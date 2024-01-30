"""Testing for Day 11"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_11")

def test_young() -> None:
    """Test cosmic_expansion with old=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        image = f.read()

    distance = aoc.cosmic_expansion(image, old=False)

    assert distance == 9536038


def test_old() -> None:
    """Test cosmic_expansion with old=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        image = f.read()

    distance = aoc.cosmic_expansion(image, old=True)

    assert distance == 447744640566
