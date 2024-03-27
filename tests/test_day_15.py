"""Testing for Day 15"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_15")

def test_sum() -> None:
    """Test lens_library with boxes=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        sequence = f.read()

    hash_sum = aoc.lens_library(sequence, boxes=False)

    assert hash_sum == 503154


def test_boxes() -> None:
    """Test lens_library with boxes=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        sequence = f.read()

    hash_sum = aoc.lens_library(sequence, boxes=True)

    assert hash_sum == 251353
