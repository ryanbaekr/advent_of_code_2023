"""Processing for Day 21"""

def step_counter(garden: str, infinite: bool) -> int:
    """Take the garden and return the appropriate value"""

    if infinite:
        steps = 26501365

        # create 2x2 garden (mega garden)
        parsed_garden = [line + line for line in garden.splitlines()] * 2

        # mega garden properties
        width = len(parsed_garden[0])
        length = len(parsed_garden)

        # start properties
        start = divmod("".join(parsed_garden).find("S"), width)

        # calculate the number of plots reachable on an odd step in the mega garden
        visited = _walk_garden(width, start, parsed_garden, 3 * width + 1)[0]

        # calculate the number of steps from S to each of the edges
        steps_to_top_edge = start[0]
        steps_to_bot_edge = (length - 1) - start[0]
        steps_to_lft_edge = start[1]
        steps_to_rgt_edge = (width - 1) - start[1]

        # calculate the number of steps from any edge to every other spot in the mega garden
        check, required_from_edge = _walk_garden(width, (length - 1, start[1]), parsed_garden, 3 * width + 1)

        # up
        remaining_steps = steps - steps_to_top_edge
        while remaining_steps > required_from_edge:
            remaining_steps -= length
            visited += check
        while remaining_steps > length:
            visited += _walk_garden(width, (length - 1, start[1]), parsed_garden, remaining_steps - 1)[0]
            remaining_steps -= length
        visited += _walk_garden(width, (length - 1, start[1]), parsed_garden, remaining_steps - 1)[0]

        # down
        remaining_steps = steps - steps_to_bot_edge
        while remaining_steps > required_from_edge:
            remaining_steps -= length
            visited += check
        while remaining_steps > length:
            visited += _walk_garden(width, (0, start[1]), parsed_garden, remaining_steps - 1)[0]
            remaining_steps -= length
        visited += _walk_garden(width, (0, start[1]), parsed_garden, remaining_steps - 1)[0]

        # left
        remaining_steps = steps - steps_to_lft_edge
        while remaining_steps > required_from_edge:
            remaining_steps -= width
            visited += check
        while remaining_steps > width:
            visited += _walk_garden(width, (start[0], width - 1), parsed_garden, remaining_steps - 1)[0]
            remaining_steps -= width
        visited += _walk_garden(width, (start[0], width - 1), parsed_garden, remaining_steps - 1)[0]

        # right
        remaining_steps = steps - steps_to_rgt_edge
        while remaining_steps > required_from_edge:
            remaining_steps -= width
            visited += check
        while remaining_steps > width:
            visited += _walk_garden(width, (start[0], 0), parsed_garden, remaining_steps - 1)[0]
            remaining_steps -= width
        visited += _walk_garden(width, (start[0], 0), parsed_garden, remaining_steps - 1)[0]

        # calculate the number of steps from S to each of the corners
        steps_to_top_left = steps_to_top_edge + steps_to_lft_edge
        steps_to_bot_left = steps_to_bot_edge + steps_to_lft_edge
        steps_to_top_rght = steps_to_top_edge + steps_to_rgt_edge
        steps_to_bot_rght = steps_to_bot_edge + steps_to_rgt_edge

        # calculate the number of steps from any corner to every other spot in the mega garden
        check, required_from_corner = _walk_garden(width, (length - 1, width - 1), parsed_garden, 3 * width + 1)

        # up left
        new_visited = []
        remaining_steps = steps - steps_to_top_left
        while remaining_steps > required_from_corner:
            remaining_steps -= width
            new_visited.append(check)
        while remaining_steps > width:
            new_visited.append(_walk_garden(width, (length - 1, width - 1), parsed_garden, remaining_steps - 2)[0])
            remaining_steps -= width
        new_visited.append(_walk_garden(width, (length - 1, width - 1), parsed_garden, remaining_steps - 2)[0])
        new_visited = [0] + new_visited
        visited += sum([x * y for x, y in zip(new_visited, list(range(len(new_visited))))])

        # down left
        new_visited = []
        remaining_steps = steps - steps_to_bot_left
        while remaining_steps > required_from_corner:
            remaining_steps -= width
            new_visited.append(check)
        while remaining_steps > width:
            new_visited.append(_walk_garden(width, (0, width - 1), parsed_garden, remaining_steps - 2)[0])
            remaining_steps -= width
        new_visited.append(_walk_garden(width, (0, width - 1), parsed_garden, remaining_steps - 2)[0])
        new_visited = [0] + new_visited
        visited += sum([x * y for x, y in zip(new_visited, list(range(len(new_visited))))])

        # up right
        new_visited = []
        remaining_steps = steps - steps_to_top_rght
        while remaining_steps > required_from_corner:
            remaining_steps -= width
            new_visited.append(check)
        while remaining_steps > width:
            new_visited.append(_walk_garden(width, (length - 1, 0), parsed_garden, remaining_steps - 2)[0])
            remaining_steps -= width
        new_visited.append(_walk_garden(width, (length - 1, 0), parsed_garden, remaining_steps - 2)[0])
        new_visited = [0] + new_visited
        visited += sum([x * y for x, y in zip(new_visited, list(range(len(new_visited))))])

        # down right
        new_visited = []
        remaining_steps = steps - steps_to_bot_rght
        while remaining_steps > required_from_corner:
            remaining_steps -= width
            new_visited.append(check)
        while remaining_steps > width:
            new_visited.append(_walk_garden(width, (0, 0), parsed_garden, remaining_steps - 2)[0])
            remaining_steps -= width
        new_visited.append(_walk_garden(width, (0, 0), parsed_garden, remaining_steps - 2)[0])
        new_visited = [0] + new_visited
        visited += sum([x * y for x, y in zip(new_visited, list(range(len(new_visited))))])

        return visited

    width = garden.find("\n")
    start = divmod(garden.replace("\n", "").find("S"), width)
    parsed_garden = garden.splitlines()

    return _walk_garden(width, start, parsed_garden, 64)[0]


def _walk_garden(width: int, start: tuple[int, int], parsed_garden: list[str], remaining_steps: int) -> tuple[int, int]:
    """Walk a single garden and return the number of plots reached"""

    queue = [start]
    visited: dict[tuple[int, int], bool] = {}
    visited_even: dict[tuple[int, int], bool] = {}

    steps_required = remaining_steps

    for index in range(remaining_steps):
        next_queue = []

        temp = len(visited)

        for coords in queue:
            line, char = coords
            # up
            new_line = line - 1
            new_char = char
            new_coords = (new_line, new_char)
            if not visited.get(new_coords, False) and new_line >= 0 and parsed_garden[new_line][new_char] in (".", "S"):
                next_queue.append(new_coords)
                visited[new_coords] = True
                if index % 2 != remaining_steps % 2:
                    visited_even[new_coords] = True
            # down
            new_line = line + 1
            new_char = char
            new_coords = (new_line, new_char)
            if not visited.get(new_coords, False) and new_line < len(parsed_garden) and parsed_garden[new_line][new_char] in (".", "S"):
                next_queue.append(new_coords)
                visited[new_coords] = True
                if index % 2 != remaining_steps % 2:
                    visited_even[new_coords] = True
            # left
            new_line = line
            new_char = char - 1
            new_coords = (new_line, new_char)
            if not visited.get(new_coords, False) and new_char >= 0 and parsed_garden[new_line][new_char] in (".", "S"):
                next_queue.append(new_coords)
                visited[new_coords] = True
                if index % 2 != remaining_steps % 2:
                    visited_even[new_coords] = True
            # right
            new_line = line
            new_char = char + 1
            new_coords = (new_line, new_char)
            if not visited.get(new_coords, False) and new_char < width and parsed_garden[new_line][new_char] in (".", "S"):
                next_queue.append(new_coords)
                visited[new_coords] = True
                if index % 2 != remaining_steps % 2:
                    visited_even[new_coords] = True

        if len(visited) == temp:
            steps_required = index
            break

        queue = next_queue

    return len(visited_even), steps_required
