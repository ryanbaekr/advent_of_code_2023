"""Testing for Day 21"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_21")

def test_normal() -> None:
    """Test step_counter with infinite=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        garden = f.read()

    steps = aoc.step_counter(garden, infinite=False)

    assert steps == 3764


def test_infinite() -> None:
    """Test step_counter with infinite=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        garden = f.read()

    steps = aoc.step_counter(garden, infinite=True)

    assert steps == 622926941971282
