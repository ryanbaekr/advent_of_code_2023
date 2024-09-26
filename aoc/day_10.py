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
            connection = (1, direction, position)
            connections.append(connection)

    for symbol in ("|", "-", "L", "J", "7", "F"):
        if all((connection[1] in symbol_maps[symbol].values() for connection in connections)):
            sketch_pt2[start] = symbol
            break

    last = -1

    loop = True
    while loop:
        for index, connection in enumerate(connections):
            sketch_pt2[connection[2]] = sketch[connection[2]]
            distance = connection[0] + 1
            direction = symbol_maps[sketch[connection[2]]][connection[1]]
            position = connection[2] + direction_map[direction]
            if position == last:
                loop = False
                break
            connections[index] = (distance, direction, position)
            last = position

    sketch_pt2[position] = sketch[position]

    start = "".join(sketch_pt2).find("F")

    connection_pt2 = ("r", start + direction_map["r"])

    while connection_pt2[1] != start:
        position_cw = connection_pt2[1] + direction_map[clockwise[connection_pt2[0]]]
        if sketch_pt2[position_cw] == ".":
            sketch_pt2[position_cw] = "I"
        direction = symbol_maps[sketch_pt2[connection_pt2[1]]][connection_pt2[0]]
        position = connection_pt2[1] + direction_map[direction]
        position_cw = connection_pt2[1] + direction_map[clockwise[direction]]
        if sketch_pt2[position_cw] == ".":
            sketch_pt2[position_cw] = "I"
        connection_pt2 = (direction, position)

    return distance, len(sketch) - len(re.sub(r"I(\.*I)*", "", "".join(sketch_pt2)))
