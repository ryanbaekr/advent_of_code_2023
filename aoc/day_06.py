"""Processing for Day 06"""

import re

def wait_for_it(records: str) -> tuple[int, int]:
    """Take the records and return the appropriate values"""

    records = re.sub(r" +", " ", records)

    lines = records.splitlines()

    distances = lines[1].split(": ")[-1].split(" ")

    product_total = 1

    for race, total_time in enumerate(lines[0].split(": ")[-1].split(" ")):
        distance = int(distances[race])
        time = int(total_time)
        product_total *= time - 1 - 2 * int((time - (time**2 - 4 * distance)**0.5)/2)

    distance = int(lines[1].split(": ")[-1].replace(" ", ""))
    time = int(lines[0].split(": ")[-1].replace(" ", ""))

    return product_total, time - 1 - 2 * int((time - (time**2 - 4 * distance)**0.5)/2)
