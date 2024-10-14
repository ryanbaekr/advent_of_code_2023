"""Processing for Day 22"""

def sand_slabs(snapshot: str) -> tuple[int, int]:
    """Take the snapshot and return the appropriate values"""

    #      z    bb   brick uid  start x    y     stop  x    y
    stack: list[list[tuple[int, tuple[int, int], tuple[int, int]]]] = []

    #                zdx       uid        start x, y, z    stop  x, y, z
    coords_map: dict[int, dict[int, tuple[tuple[int, ...], tuple[int, ...]]]] = {}

    chains: list[list[int]] = []
    counts: dict[int, int] = {}
    ancestors: dict[int, list[int]] = {}

    for uid, coords_str in enumerate(snapshot.splitlines()):
        start_str, stop_str = coords_str.split("~")
        start = tuple([int(num) for num in start_str.split(",")])  # x, y, z
        stop = tuple([int(num) for num in stop_str.split(",")])  # x, y, z

        zdx = start[2]
        try:
            coords_map[zdx][uid] = (start, stop)
        except KeyError:
            coords_map[zdx] = {uid: (start, stop)}

    total_bricks = uid + 1
    sole_support = []

    for zdx in sorted(coords_map.keys()):
        for uid, bb in coords_map[zdx].items():
            start, stop = bb

            if len(stack) == 0:
                for _ in range(stop[2] - start[2] + 1):
                    stack.append(
                        [
                            (uid, (start[0], start[1]), (stop[0], stop[1]))
                        ]
                    )
                chains.append([uid])
                counts[uid] = 0
                ancestors[uid] = []
                continue

            for z in range(len(stack) -1, -1, -1):
                supporting = []
                for s_bb in stack[z]:
                    s_uid, s_start, s_stop = s_bb
                    if (start[0] <= s_stop[0] and stop[0] >= s_start[0]) and (start[1] <= s_stop[1] and stop[1] >= s_start[1]):
                        supporting.append(s_uid)
                if len(supporting) != 0:
                    for chain in chains:
                        if all(support in chain for support in supporting):
                            chain.append(uid)
                            if len(supporting) == 1:
                                ancestors[uid] = [supporting[0]] + ancestors[supporting[0]].copy()
                                counts[uid] = counts[supporting[0]] + 1
                            else:
                                testing = ancestors[supporting[0]].copy()
                                for support in supporting:
                                    while testing[0] not in ancestors[support]:
                                        testing = testing[1:]
                                ancestors[uid] = [testing[0]] + ancestors[testing[0]].copy()
                                counts[uid] = counts[testing[0]] + 1
                            break
                    else:
                        chains.append([uid])
                        counts[uid] = 0
                        ancestors[uid] = []
                    if len(supporting) == 1:
                        sole_support.extend(supporting)
                    for i in range(stop[2] - start[2] + 1):
                        try:
                            stack[z + i + 1].append(
                                (uid, (start[0], start[1]), (stop[0], stop[1]))
                            )
                        except IndexError:
                            stack.append(
                                [
                                    (uid, (start[0], start[1]), (stop[0], stop[1]))
                                ]
                            )
                    break

            if len(supporting) == 0:
                for i in range(stop[2] - start[2] + 1):
                    try:
                        stack[i].append(
                            (uid, (start[0], start[1]), (stop[0], stop[1]))
                        )
                    except IndexError:
                        stack.append(
                            [
                                (uid, (start[0], start[1]), (stop[0], stop[1]))
                            ]
                        )
                chains.append([uid])
                counts[uid] = 0
                ancestors[uid] = []

    chain_sum = 0
    for chain in chains:
        for uid in chain:
            chain_sum += counts[uid]

    return total_bricks - len(set(sole_support)), chain_sum
