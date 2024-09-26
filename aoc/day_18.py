"""Processing for Day 18"""

def lavaduct_lagoon(dig_plan: str, rgb: bool) -> int:
    """Take the plan and return the appropriate value"""

    parsed_dig_plan = dig_plan.splitlines()

    rgb_map = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U",
    }

    rot_map = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
    }

    l_pos = 0
    c_pos = 0

    vertices = []

    perim = 2

    for instruction in parsed_dig_plan:
        if rgb:
            _, _, dur_str = instruction.split(" ")
            rot = rgb_map[dur_str[-2]]
            dur = int(dur_str[2:-2], 16)
        else:
            rot, dur_str, _ = instruction.split(" ")
            dur = int(dur_str)

        l_inc, c_inc = rot_map[rot]
        l_pos += l_inc * dur
        c_pos += c_inc * dur

        vertices.append((l_pos, c_pos))

        perim += dur

    area = 0

    for i in range(len(vertices)):
        area += (vertices[i - 1][0] + vertices[i][0]) * (vertices[i - 1][1] - vertices[i][1])

    return abs((area + perim) // 2)
