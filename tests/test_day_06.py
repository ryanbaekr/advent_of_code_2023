"""Testing for Day 06"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_06")

def test_sums() -> None:
    """Test wait_for_it"""

    with open(FIXTURE, encoding="utf-8") as f:
        records = f.read()

    product_total, kerning_total = aoc.wait_for_it(records)

    assert product_total == 633080
    assert kerning_total == 20048741
