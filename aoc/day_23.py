"""Processing for Day 23"""

def a_long_walk(trails: str, traction: bool) -> int:
    """Take the trails and return the appropriate value"""

    if traction:
        trails = trails.replace("^", ".").replace("v", ".").replace("<", ".").replace(">", ".")

    ptrails = trails.splitlines()

    begin = (0, ptrails[0].find("."))
    end = (len(ptrails) - 1, ptrails[-1].find("."))

    l_map = {
        "u": -1,
        "d": 1,
        "l": 0,
        "r": 0,
    }

    c_map = {
        "u": 0,
        "d": 0,
        "l": -1,
        "r": 1,
    }

    #               start l,   c                stop  l,   c     dist
    junctions: dict[tuple[int, int], list[tuple[tuple[int, int], int]]] = {}

    #                 start l,   c     prev  l,   c     current l, c     rev   dist
    queue: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int], bool, int]] = [(begin, (-1, -1), begin, True, 0)]

    while queue:
        next_queue: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int], bool, int]] = []

        for start, prev, current, rev, dist in queue:
            if current == end:
                try:
                    junctions[start].append((current, dist))
                except KeyError:
                    junctions[start] = [(current, dist)]

                #if rev:
                #    try:
                #        junctions[current].append((start, dist))
                #    except KeyError:
                #        junctions[current] = [(start, dist)]

                continue

            l, c = current

            new_positions: list[tuple[int, int]] = []

            # up
            new_l = l + l_map["u"]
            new_c = c + c_map["u"]
            if new_l >= 0 and (new_l, new_c) != prev and ptrails[new_l][new_c] in (".", "^"):
                new_positions.append((new_l, new_c))

            # down
            new_l = l + l_map["d"]
            new_c = c + c_map["d"]
            if new_l < len(ptrails) and (new_l, new_c) != prev and ptrails[new_l][new_c] in (".", "v"):
                new_positions.append((new_l, new_c))

            # left
            new_l = l + l_map["l"]
            new_c = c + c_map["l"]
            if new_c >= 0 and (new_l, new_c) != prev and ptrails[new_l][new_c] in (".", "<"):
                new_positions.append((new_l, new_c))

            # right
            new_l = l + l_map["r"]
            new_c = c + c_map["r"]
            if new_c < len(ptrails[0]) and (new_l, new_c) != prev and ptrails[new_l][new_c] in (".", ">"):
                new_positions.append((new_l, new_c))

            if len(new_positions) == 1:
                next_queue.append((start, current, new_positions[0], (rev and ptrails[new_positions[0][0]][new_positions[0][1]] == "."), dist + 1))
                continue

            try:
                if (current, dist) in junctions[start]:
                    continue
                junctions[start].append((current, dist))
            except KeyError:
                junctions[start] = [(current, dist)]

            #if rev:
            #    try:
            #        junctions[current].append((start, dist))
            #    except KeyError:
            #        junctions[current] = [(start, dist)]

            for new_position in new_positions:
                next_queue.append((current, current, new_position, (ptrails[new_position[0]][new_position[1]] == "."), 1))

        queue = next_queue

    return bellman_ford(junctions, begin)[end][0] * -1


def bellman_ford(graph: dict[tuple[int, int], list[tuple[tuple[int, int], int]]], source: tuple[int, int]) -> dict[tuple[int, int], tuple[int, dict[tuple[int, int], bool]]]:

    def update_children(parent: tuple[int, int], distance: tuple[int, dict[tuple[int, int], bool]]) -> dict[tuple[int, int], tuple[int, dict[tuple[int, int], bool]]]:
        distances: dict[tuple[int, int], tuple[int, dict[tuple[int, int], bool]]] = {}
        distances[parent] = distance

        for child, dist in graph[parent]:
            if child in distance[1]:
                continue
            if child in graph:
                temp_dict = distance[1].copy()
                temp_dict[parent] = True
                temp_distances = update_children(child, (distance[0] - dist, temp_dict))
                for source, info in temp_distances.items():
                    if source in distances:
                        if info[0] < distances[source][0]:
                            distances[source] = info
                    else:
                        distances[source] = info
            elif distance[0] - dist < distances.get(child, (0, []))[0]:
                temp_dict = distance[1].copy()
                temp_dict[parent] = True
                distances[child] = (distance[0] - dist, temp_dict)

        return distances

    distances = update_children(source, (0, {}))

    return distances
