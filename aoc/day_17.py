"""Processing for Day 17"""

import heapq

def clumsy_crucible(city_map: str, ultra: bool) -> int:
    """Take the map and return the appropriate value"""

    city_map = [[int(char) for char in line] for line in city_map.splitlines()]

    loss_list = [(0, " 9", 0, 0)]

    seen = set()
    mins = {(" 9", 0, 0): 0}

    while True:
        loss, path, l_idx, c_idx = heapq.heappop(loss_list)

        if (path, l_idx, c_idx) in seen:
            continue

        if l_idx == 140 and c_idx == 140:
            return loss

        # up
        if l_idx > 0 and path[0] != "d" and ((not ultra and path != "u3") or (ultra and path != "u10" and (int(path[1:]) >= 4 or path[0] == "u"))):
            if path[0] == "u":
                new_path = f"u{int(path[1:]) + 1}"
            else:
                new_path = "u1"
            new_l_idx = l_idx - 1
            new_c_idx = c_idx
            new_name = (new_path, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_path, new_l_idx, new_c_idx))

        # down
        if l_idx < 140 and path[0] != "u" and ((not ultra and path != "d3") or (ultra and path != "d10" and (int(path[1:]) >= 4 or path[0] == "d"))):
            if path[0] == "d":
                new_path = f"d{int(path[1:]) + 1}"
            else:
                new_path = "d1"
            new_l_idx = l_idx + 1
            new_c_idx = c_idx
            new_name = (new_path, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_path, new_l_idx, new_c_idx))

        # left
        if c_idx > 0 and path[0] != "r" and ((not ultra and path != "l3") or (ultra and path != "l10" and (int(path[1:]) >= 4 or path[0] == "l"))):
            if path[0] == "l":
                new_path = f"l{int(path[1:]) + 1}"
            else:
                new_path = "l1"
            new_l_idx = l_idx
            new_c_idx = c_idx - 1
            new_name = (new_path, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_path, new_l_idx, new_c_idx))

        # right
        if c_idx < 140 and path[0] != "l" and ((not ultra and path != "r3") or (ultra and path != "r10" and (int(path[1:]) >= 4 or path[0] == "r"))):
            if path[0] == "r":
                new_path = f"r{int(path[1:]) + 1}"
            else:
                new_path = "r1"
            new_l_idx = l_idx
            new_c_idx = c_idx + 1
            new_name = (new_path, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_path, new_l_idx, new_c_idx))

        seen.add((path, l_idx, c_idx))
