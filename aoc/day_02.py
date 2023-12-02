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

            if color == "red":
                if quantity > 12:
                    game_id = 0
                if quantity > red_max:
                    red_max = quantity
            elif color == "green":
                if quantity > 13:
                    game_id = 0
                if quantity > green_max:
                    green_max = quantity
            elif color == "blue":
                if quantity > 14:
                    game_id = 0
                if quantity > blue_max:
                    blue_max = quantity

        valid_sum += game_id
        power_sum += red_max * green_max * blue_max

    return valid_sum, power_sum
