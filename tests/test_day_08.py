"""Testing for Day 08"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_08")

def test_as_human() -> None:
    """Test haunted_wasteland with as_ghost=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        documents = f.read()

    steps = aoc.haunted_wasteland(documents, as_ghost=False)

    assert steps == 13019


def test_as_ghost() -> None:
    """Test haunted_wasteland with as_ghost=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        documents = f.read()

    steps = aoc.haunted_wasteland(documents, as_ghost=True)

    assert steps == 13524038372771
