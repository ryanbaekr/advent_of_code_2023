"""Testing for Day 20"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_20")

def test_product() -> None:
    """Test pulse_propagation with product=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        configuration = f.read()

    product = aoc.pulse_propagation(configuration, product=True)

    assert product == 791120136


def test_presses() -> None:
    """Test pulse_propagation with product=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        configuration = f.read()

    presses = aoc.pulse_propagation(configuration, product=False)

    assert presses == 215252378794009
