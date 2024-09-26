"""Processing for Day 04"""

import re

def scratchcards(tickets: str) -> tuple[int, int]:
    """Take the tickets and return the appropriate values"""

    tickets = re.sub(r" +", " ", tickets)

    lines = tickets.splitlines()

    points = 0
    scrots = [1] * len(lines)

    for l_num, line in enumerate(lines):
        parsed_line = line.split(": ")[-1].split(" | ")
        matches = len(set(parsed_line[0].split(" ")) & set(parsed_line[1].split(" ")))
        points += int(2**(matches - 1))
        for jdx in range(l_num + 1, matches + l_num + 1):
            scrots[jdx] += scrots[l_num]

    return points, sum(scrots)
