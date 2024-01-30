"""Processing for Day 11"""

def cosmic_expansion(image: str, old: bool) -> int:
    """Take the image and return the appropriate value"""

    if old:
        offset = 999999
    else:
        offset = 1

    lines = image.splitlines()

    positions = []

    l_offset = 0
    for l_num, line in enumerate(lines):
        if "#" not in line:
            l_offset += offset
            continue
        c_offset = 0
        for c_num, char in enumerate(line):
            if char == "#":
                positions.append((l_num + l_offset, c_num + c_offset))
            elif "#" not in [line[c_num] for line in lines]:
                c_offset += offset

    distance = 0

    for p_num, from_pos in enumerate(positions):
        for to_pos in positions[p_num:]:
            distance += abs(to_pos[0] - from_pos[0]) + abs(to_pos[1] - from_pos[1])

    return distance
