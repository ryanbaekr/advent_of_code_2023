"""Processing for Day 10"""

import re

def pipe_maze(sketch: str) -> tuple[int, int]:
    """Take the sketch and return the appropriate values"""

    width = sketch.find("\n")

    sketch = sketch.replace("\n", "")

    sketch_pt2 = ["."] * len(sketch)

    direction_map = {
        "u": -width,
        "d": width,
        "l": -1,
        "r": 1,
    }

    symbol_maps = {
        "|": {
            "u": "u",
            "d": "d",
        },
        "-": {
            "l": "l",
            "r": "r",
        },
        "L": {
            "l": "u",
            "d": "r",
        },
        "J": {
            "r": "u",
            "d": "l",
        },
        "7": {
            "r": "d",
            "u": "l",
        },
        "F": {
            "l": "d",
            "u": "r",
        },
    }

    clockwise = {
        "u": "r",
        "d": "l",
        "l": "u",
        "r": "d",
    }

    connections = []

    start = sketch.find("S")

    for direction in ("u", "d", "l", "r"):
        position = start + direction_map[direction]
        if sketch[position] != "." and direction in symbol_maps[sketch[position]]:
            connection = {
                "distance": 1,
                "direction": direction,
                "position": position,
            }
            connections.append(connection)

    for symbol in ("|", "-", "L", "J", "7", "F"):
        if all((connection["direction"] in symbol_maps[symbol].values() for connection in connections)):
            sketch_pt2[start] = symbol
            break

    last = -1

    loop = True
    while loop:
        for connection in connections:
            sketch_pt2[connection["position"]] = sketch[connection["position"]]
            distance = connection["distance"] + 1
            direction = symbol_maps[sketch[connection["position"]]][connection["direction"]]
            position = connection["position"] + direction_map[direction]
            if position == last:
                loop = False
                break
            connection["distance"] = distance
            connection["direction"] = direction
            connection["position"] = position
            last = position

    sketch_pt2[position] = sketch[position]

    start = "".join(sketch_pt2).find("F")

    connection = {
        "direction": "r",
        "position": start + direction_map["r"],
    }

    while connection["position"] != start:
        position_cw = connection["position"] + direction_map[clockwise[connection["direction"]]]
        if sketch_pt2[position_cw] == ".":
            sketch_pt2[position_cw] = "I"
        direction = symbol_maps[sketch_pt2[connection["position"]]][connection["direction"]]
        position = connection["position"] + direction_map[direction]
        position_cw = connection["position"] + direction_map[clockwise[direction]]
        if sketch_pt2[position_cw] == ".":
            sketch_pt2[position_cw] = "I"
        connection["direction"] = direction
        connection["position"] = position

    sketch_pt2 = re.sub(r"I(\.*I)*", "", "".join(sketch_pt2))

    return distance, len(sketch) - len(sketch_pt2)
