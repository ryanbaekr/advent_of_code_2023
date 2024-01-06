"""Processing for Day 08"""

from math import lcm

def haunted_wasteland(documents: str, as_ghost: bool) -> int:
    """Take the documents and return the appropriate value"""

    lines = documents.splitlines()

    directions = [int(direction) for direction in lines[0].replace("L", "0").replace("R", "1")]

    states = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

    if as_ghost:
        positions = [position for position in states if position.endswith("A")]
        step_list = []

        for state in positions:
            steps = 0

            while not state.endswith("Z"):
                for direction in directions:
                    state = states[state][direction]
                    steps += 1
                    if state.endswith("Z"):
                        break

            step_list.append(steps)

        return lcm(*step_list)

    state = "AAA"
    steps = 0

    while state != "ZZZ":
        for direction in directions:
            state = states[state][direction]
            steps += 1
            if state == "ZZZ":
                break

    return steps
