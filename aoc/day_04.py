"""Processing for Day 04"""

import re

def scratchcards(tickets: str) -> tuple[int, int]:
    """Take the tickets and return the appropriate values"""

    tickets = re.sub(r" +", " ", tickets)

    lines = tickets.splitlines()

    points = 0
    scrots = [1] * len(lines)

    for l_num, line in enumerate(lines):
        line = line.split(": ")[-1].split(" | ")
        my_nums = [int(num) for num in line[0].split(" ")]
        winning_nums = [int(num) for num in line[1].split(" ")]
        temp = len(set(my_nums) & set(winning_nums))
        if temp:
            points += 2**(temp - 1)
        for jdx in range(temp):
            scrots[l_num+jdx+1] += 1 * scrots[l_num]

    return points, sum(scrots)
