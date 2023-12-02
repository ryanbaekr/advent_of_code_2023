"""Processing for Day 02"""

def cube_conundrum(records: str) -> tuple[int, int]:
    """Take the records and return the appriate values"""

    lines = records.splitlines()

    valid_sum = 0
    power_sum = 0

    for line in lines:
        line = line.split(": ")

        game_id = int(line[0].split(" ")[-1])

        game_sets = line[1].replace(";", ",").split(", ")

        red_max = 0
        green_max = 0
        blue_max = 0

        for game_set in game_sets:
            quantity, color = game_set.split(" ")
            quantity = int(quantity)

            if color == "red" and quantity > red_max:
                red_max = quantity
            elif color == "green" and quantity > green_max:
                green_max = quantity
            elif color == "blue" and quantity > blue_max:
                blue_max = quantity

        if red_max <= 12 and green_max <= 13 and blue_max <= 14:
            valid_sum += game_id
        power_sum += red_max * green_max * blue_max

    return valid_sum, power_sum
