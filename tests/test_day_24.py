"""Testing for Day 24"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_24")

def test_normal() -> None:
    """Test never_tell_me_the_odds with rock=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        hailstones = f.read()

    intersections = aoc.never_tell_me_the_odds(hailstones, rock=False)

    assert intersections == 18184


def test_rock() -> None:
    """Test never_tell_me_the_odds with rock=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        hailstones = f.read()

    intersections = aoc.never_tell_me_the_odds(hailstones, rock=True)

    assert intersections == 557789988450159
