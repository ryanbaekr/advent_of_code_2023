"""Testing for Day 10"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_10")

def test_maze() -> None:
    """Test pipe_maze"""

    with open(FIXTURE, encoding="utf-8") as f:
        sketch = f.read()

    distance, area = aoc.pipe_maze(sketch)

    assert distance == 7086
    assert area == 317
