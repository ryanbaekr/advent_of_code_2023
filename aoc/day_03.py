"""Processing for Day 03"""

import re

def gear_ratios(schematic: str) -> tuple[int, int]:
    """Take a schematic and return the appropriate values"""

    lines = schematic.splitlines()

    part_sum = 0
    gear_sum = 0

    for l_num in range(1, len(lines) - 1):
        last_line = lines[l_num - 1]
        this_line = lines[l_num]
        next_line = lines[l_num + 1]
        for c_num in range(3, len(this_line) - 3):
            if this_line[c_num] not in ["*", "/", "$", "+", "&", "@", "#", "%", "=", "-"]:
                continue

            gear_pwr = [0]
            if this_line[c_num - 1].isdigit():
                attempt = int(re.sub(r"^\d?[^\d]+", "", this_line[c_num - 3:c_num]))
                part_sum += attempt
                gear_pwr.append(attempt)
            if this_line[c_num + 1].isdigit():
                attempt = int(re.sub(r"[^\d]+\d?$", "", this_line[c_num + 1:c_num + 4]))
                part_sum += attempt
                gear_pwr.append(attempt)
            for line in (last_line, next_line):
                if line[c_num].isdigit():
                    attempt = int(re.sub(r"(^\d?[^\d]+|[^\d]+\d?$)", "", line[c_num - 2:c_num + 3]))
                    part_sum += attempt
                    gear_pwr.append(attempt)
                else:
                    if line[c_num - 1].isdigit():
                        attempt = int(re.sub(r"^\d?[^\d]+", "", line[c_num - 3:c_num]))
                        part_sum += attempt
                        gear_pwr.append(attempt)
                    if line[c_num + 1].isdigit():
                        attempt = int(re.sub(r"[^\d]+\d?$", "", line[c_num + 1:c_num + 4]))
                        part_sum += attempt
                        gear_pwr.append(attempt)
            gear_sum += gear_pwr[-2] * gear_pwr[-1] * (this_line[c_num] == "*")

    return part_sum, gear_sum
