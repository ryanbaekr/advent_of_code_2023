"""Testing for Day 07"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_07")

def test_as_jack() -> None:
    """Test camel_cards with as_wild=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        hands = f.read()

    score = aoc.camel_cards(hands, as_wild=False)

    assert score == 251545216


def test_as_wild() -> None:
    """Test camel_cards with as_wild=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        hands = f.read()

    score = aoc.camel_cards(hands, as_wild=True)

    assert score == 250384185
