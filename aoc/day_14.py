"""Processing for Day 14"""

import functools

def parabolic_reflector_dish(positions: str, spin: bool) -> int:
    """Take the positions and return the appropriate value"""

    load = 0

    # switch to east so we properly switch to north
    parsed_positions = [line[::-1] for line in positions.splitlines()]

    if spin:
        positions_str_list: list[str] = []
        cycle = 1
        while cycle <= 1000000000:
            for direction in ("n", "w", "s", "e"):
                if direction == "n":
                    parsed_positions = ["".join([line[c_idx] for line in parsed_positions]) for c_idx in range(len(parsed_positions[0])-1, -1, -1)]
                elif direction == "s":
                    parsed_positions = ["".join([line[c_idx] for line in parsed_positions])[::-1] for c_idx in range(len(parsed_positions[0]))]
                elif direction == "e":
                    parsed_positions = ["".join([line[c_idx] for line in parsed_positions])[::-1] for c_idx in range(len(parsed_positions[0]))][::-1]
                else:
                    parsed_positions = ["".join([line[c_idx] for line in parsed_positions]) for c_idx in range(len(parsed_positions[0]))]

                parsed_positions = [_shift_rocks(line) for line in parsed_positions]

            positions_str = "\n".join(parsed_positions)
            if positions_str in positions_str_list:
                for index, item in enumerate(positions_str_list):
                    if item == positions_str:
                        break
                positions_str_list = positions_str_list[index::]
                index = (1000000000 - cycle) % len(positions_str_list)
                parsed_positions = positions_str_list[index].splitlines()
                break
            positions_str_list.append(positions_str)
            cycle += 1

        # switch back to north one last time
        parsed_positions = ["".join([line[c_idx] for line in parsed_positions]) for c_idx in range(len(parsed_positions[0])-1, -1, -1)]
    else:
        parsed_positions = ["".join([line[c_idx] for line in parsed_positions]) for c_idx in range(len(parsed_positions[0])-1, -1, -1)]
        parsed_positions = [_shift_rocks(line) for line in parsed_positions]

    max_load = len(parsed_positions[0])

    for line in parsed_positions:
        for c_idx, char in enumerate(line):
            if char == "O":
                load += max_load - c_idx

    return load


@functools.lru_cache(maxsize=512)
def _shift_rocks(line: str) -> str:
    """Function to shift all rocks in a line"""

    return "#".join(["".join(sorted(part, reverse=True)) for part in line.split("#")])
