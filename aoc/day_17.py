"""Processing for Day 17"""

import heapq

def clumsy_crucible(city_map: str, ultra: bool) -> int:
    """Take the map and return the appropriate value"""

    if ultra:
        min_dur = 4
        max_dur = 10
    else:
        min_dur = 1
        max_dur = 3

    city_map = [[int(char) for char in line] for line in city_map.splitlines()]

    loss_list = [(0, " ", 9, 0, 0)]

    seen = set()
    mins = {(" ", 9, 0, 0): 0}

    while True:
        loss, rot, dur, l_idx, c_idx = heapq.heappop(loss_list)

        if (rot, dur, l_idx, c_idx) in seen:
            continue

        if l_idx == 140 and c_idx == 140:
            return loss

        # up
        if l_idx > 0 and rot != "d" and ((rot != "u" and dur >= min_dur) or (rot == "u" and dur < max_dur)):
            new_rot = "u"
            if rot == "u":
                new_dur = dur + 1
            else:
                new_dur = 1
            new_l_idx = l_idx - 1
            new_c_idx = c_idx
            new_name = (new_rot, new_dur, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_rot, new_dur, new_l_idx, new_c_idx))

        # down
        if l_idx < 140 and rot != "u" and ((rot != "d" and dur >= min_dur) or (rot == "d" and dur < max_dur)):
            new_rot = "d"
            if rot == "d":
                new_dur = dur + 1
            else:
                new_dur = 1
            new_l_idx = l_idx + 1
            new_c_idx = c_idx
            new_name = (new_rot, new_dur, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_rot, new_dur, new_l_idx, new_c_idx))

        # left
        if c_idx > 0 and rot != "r" and ((rot != "l" and dur >= min_dur) or (rot == "l" and dur < max_dur)):
            new_rot = "l"
            if rot == "l":
                new_dur = dur + 1
            else:
                new_dur = 1
            new_l_idx = l_idx
            new_c_idx = c_idx - 1
            new_name = (new_rot, new_dur, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_rot, new_dur, new_l_idx, new_c_idx))

        # right
        if c_idx < 140 and rot != "l" and ((rot != "r" and dur >= min_dur) or (rot == "r" and dur < max_dur)):
            new_rot = "r"
            if rot == "r":
                new_dur = dur + 1
            else:
                new_dur = 1
            new_l_idx = l_idx
            new_c_idx = c_idx + 1
            new_name = (new_rot, new_dur, new_l_idx, new_c_idx)

            if new_name not in seen:
                prev = mins.get(new_name)
                new_loss = loss + city_map[new_l_idx][new_c_idx]
                if prev is None or new_loss < prev:
                    mins[new_name] = new_loss
                    heapq.heappush(loss_list, (new_loss, new_rot, new_dur, new_l_idx, new_c_idx))

        seen.add((rot, dur, l_idx, c_idx))
