"""Processing for Day 16"""

def the_floor_will_be_lava(layout: str, best: bool) -> int:
    """Take the layout and return the appropriate value"""

    parsed_layout = [list(line) for line in layout.splitlines()]

    symbol_maps = {
        "|": {
            "u": "u",
            "d": "d",
            "l": "ud",
            "r": "ud",
        },
        "-": {
            "u": "lr",
            "d": "lr",
            "l": "l",
            "r": "r",
        },
        "\\": {
            "u": "l",
            "d": "r",
            "l": "u",
            "r": "d",
        },
        "/": {
            "u": "r",
            "d": "l",
            "l": "d",
            "r": "u",
        },
        ".": {
            "u": "u",
            "d": "d",
            "l": "l",
            "r": "r",
        }
    }

    l_map = {
        "u": -1,
        "d": 1,
        "l": 0,
        "r": 0,
    }

    c_map = {
        "u": 0,
        "d": 0,
        "l": -1,
        "r": 1,
    }

    def _helper(l_idx: int, c_idx: int, direction: str) -> None:
        """Function to recurse with"""

        positions[f"{l_idx}c{c_idx}{direction}"] = True
        direction = symbol_maps[parsed_layout[l_idx][c_idx]][direction]

        while len(direction) == 1:
            l_idx = l_idx + l_map[direction]
            c_idx = c_idx + c_map[direction]
            temp = f"{l_idx}c{c_idx}{direction}"
            if not (0 <= l_idx < 110 and 0 <= c_idx < 110) or positions.get(temp, False):
                return
            positions[temp] = True
            direction = symbol_maps[parsed_layout[l_idx][c_idx]][direction]

        for new_direction in direction:
            new_l_idx = l_idx + l_map[new_direction]
            new_c_idx = c_idx + c_map[new_direction]
            if not (0 <= new_l_idx < 110 and 0 <= new_c_idx < 110) or \
                    positions.get(f"{new_l_idx}c{new_c_idx}{new_direction}", False):
                continue
            _helper(new_l_idx, new_c_idx, new_direction)

    result = 0

    if best:
        starts = []
        for index in range(110):
            starts.extend(
                [
                    (0, index, "d"),
                    (109, index, "u"),
                    (index, 0, "r"),
                    (index, 109, "l")
                ]
            )
    else:
        starts = [(0, 0, "r")]

    for start in starts:
        positions: dict[str, bool] = {}
        _helper(*start)
        result = max(result, len({pos[:-1] for pos in positions}))

    return result
