"""Processing for Day 03"""

def gear_ratios(schematic: str) -> tuple[int, int]:
    """Take a schematic and return the appropriate values"""

    lines = schematic.splitlines()

    part_sum = 0
    part_str = "0"
    part_use = False

    gear_sum = 0
    gear_map = {}
    gear_key = ""

    for line_num in range(len(lines)):
        line = lines[line_num]
        for char_num in range(len(line)):
            char = line[char_num]
            if char.isdigit():
                part_str += char
                if not part_use:
                    for row, col in [(line_num-1, char_num-1), (line_num-1, char_num), (line_num-1, char_num+1), (line_num, char_num-1), (line_num, char_num+1), (line_num+1, char_num-1), (line_num+1, char_num), (line_num+1, char_num+1)]:
                        if row < len(lines) and col < len(line):
                            check_char = lines[row][col]
                            if check_char in ["*", "/", "$", "+", "&", "@", "#", "%", "=", "-"]:
                                part_use = True
                                gear_key = check_char + str(row) + "," + str(col)
                                break
            else:
                part_num = int(part_str) * part_use
                if gear_key.startswith("*"):
                    gear_sum += gear_map.get(gear_key, 0) * part_num
                    gear_map[gear_key] = part_num
                    gear_key = ""
                part_sum += part_num
                part_str = "0"
                part_use = False

    return part_sum, gear_sum
