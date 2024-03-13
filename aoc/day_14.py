"""Processing for Day 14"""

def parabolic_reflector_dish(positions: str, spin: bool) -> int:
    """Take the positions and return the appropriate value"""

    load = 0

    # switch to east so we properly switch to north
    positions = [list(line[::-1]) for line in positions.splitlines()]

    positions_str_list = []

    if spin:
        cycle = 1
        while cycle <= 1000000000:
            for direction in ("n", "w", "s", "e"):
                if direction == "n":
                    positions = [[line[c_idx] for line in positions] for c_idx in range(len(positions[0])-1, -1, -1)]
                elif direction == "s":
                    positions = [[line[c_idx] for line in positions][::-1] for c_idx in range(len(positions[0]))]
                elif direction == "e":
                    positions = [[line[c_idx] for line in positions][::-1] for c_idx in range(len(positions[0]))][::-1]
                else:
                    positions = [[line[c_idx] for line in positions] for c_idx in range(len(positions[0]))]

                for l_idx, line in enumerate(positions):
                    next_load = 0
                    for c_idx, char in enumerate(line):
                        if char == "O":
                            line[c_idx] = "."
                            line[next_load] = "O"
                            next_load += 1
                        elif char == "#":
                            next_load = c_idx + 1
                    positions[l_idx] = line

            positions_str = "\n".join(["".join(line) for line in positions])
            if positions_str in positions_str_list:
                for index, item in enumerate(positions_str_list):
                    if item == positions_str:
                        break
                positions_str_list = positions_str_list[index::]
                index = (1000000000 - cycle) % len(positions_str_list)
                positions = [list(line) for line in positions_str_list[index].splitlines()]
                break
            positions_str_list.append(positions_str)
            cycle += 1

        # switch back to north one last time
        positions = [[line[c_idx] for line in positions] for c_idx in range(len(positions[0])-1, -1, -1)]
    else:
        positions = [[line[c_idx] for line in positions] for c_idx in range(len(positions[0])-1, -1, -1)]
        for l_idx, line in enumerate(positions):
            next_load = 0
            for c_idx, char in enumerate(line):
                if char == "O":
                    line[c_idx] = "."
                    line[next_load] = "O"
                    next_load += 1
                elif char == "#":
                    next_load = c_idx + 1
            positions[l_idx] = line

    max_load = len(positions[0])

    for line in positions:
        next_load = max_load
        for c_idx, char in enumerate(line):
            if char == "O":
                load += max_load - c_idx

    return load
