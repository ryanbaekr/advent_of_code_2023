"""Testing for Day 01"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_01")

def test_numeric_only() -> None:
    """Test trebuchet with as_word=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        document = f.read()

    output = aoc.trebuchet(document, as_word=False)

    assert output == 55108


def test_as_word() -> None:
    """Test trebuchet with as_word=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        document = f.read()

    output = aoc.trebuchet(document, as_word=True)

    assert output == 56324
