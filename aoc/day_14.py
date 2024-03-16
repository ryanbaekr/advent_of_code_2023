"""Processing for Day 14"""

import functools

def parabolic_reflector_dish(positions: str, spin: bool) -> int:
    """Take the positions and return the appropriate value"""

    load = 0

    # switch to east so we properly switch to north
    positions = [line[::-1] for line in positions.splitlines()]

    if spin:
        positions_str_list = []
        cycle = 1
        while cycle <= 1000000000:
            for direction in ("n", "w", "s", "e"):
                if direction == "n":
                    positions = ["".join([line[c_idx] for line in positions]) for c_idx in range(len(positions[0])-1, -1, -1)]
                elif direction == "s":
                    positions = ["".join([line[c_idx] for line in positions])[::-1] for c_idx in range(len(positions[0]))]
                elif direction == "e":
                    positions = ["".join([line[c_idx] for line in positions])[::-1] for c_idx in range(len(positions[0]))][::-1]
                else:
                    positions = ["".join([line[c_idx] for line in positions]) for c_idx in range(len(positions[0]))]

                positions = [_shift_rocks(line) for line in positions]

            positions_str = "\n".join(positions)
            if positions_str in positions_str_list:
                for index, item in enumerate(positions_str_list):
                    if item == positions_str:
                        break
                positions_str_list = positions_str_list[index::]
                index = (1000000000 - cycle) % len(positions_str_list)
                positions = positions_str_list[index].splitlines()
                break
            positions_str_list.append(positions_str)
            cycle += 1

        # switch back to north one last time
        positions = ["".join([line[c_idx] for line in positions]) for c_idx in range(len(positions[0])-1, -1, -1)]
    else:
        positions = ["".join([line[c_idx] for line in positions]) for c_idx in range(len(positions[0])-1, -1, -1)]
        positions = [_shift_rocks(line) for line in positions]

    max_load = len(positions[0])

    for line in positions:
        for c_idx, char in enumerate(line):
            if char == "O":
                load += max_load - c_idx

    return load


@functools.lru_cache(maxsize=512)
def _shift_rocks(line):
    """Function to shift all rocks in a line"""

    return "#".join(["".join(sorted(part, reverse=True)) for part in line.split("#")])
