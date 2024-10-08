"""Processing for Day 02"""

def cube_conundrum(records: str) -> tuple[int, int]:
    """Take the records and return the appriate values"""

    lines = records.splitlines()

    valid_sum = 0
    power_sum = 0

    for line in lines:
        parsed_line = line.split(": ")

        game_id = int(parsed_line[0].split(" ")[-1])

        game_sets = parsed_line[1].replace(";", ",").split(", ")

        need = {"red": 0, "green": 0, "blue": 0}

        for game_set in game_sets:
            quantity, color = game_set.split(" ")

            need[color] = max(need[color], int(quantity))

        valid_sum += game_id * (need["red"] <= 12 and need["green"] <= 13 and need["blue"] <= 14)
        power_sum += need["red"] * need["green"] * need["blue"]

    return valid_sum, power_sum
