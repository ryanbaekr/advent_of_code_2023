"""Testing for Day 25"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_25")

def test_normal() -> None:
    """Test snowverload"""

    with open(FIXTURE, encoding="utf-8") as f:
        diagram = f.read()

    product = aoc.snowverload(diagram)

    assert product == 550080
