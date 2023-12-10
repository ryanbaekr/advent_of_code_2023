"""Processing for Day 05"""

def if_you_give_a_seed_a_fertilizer(almanac: str, as_range: bool) -> int:
    """Take an almanac and return the appropriate value"""

    seed_ranges = []
    temp_ranges = []
    map_name = ""

    for line in almanac.splitlines():
        if line.startswith("seeds: "):
            seeds = [int(num) for num in line.split(": ")[1].split(" ")]
            if as_range:
                seed_ranges = [(seeds[n], seeds[n] + seeds[n + 1]) for n in range(0, len(seeds), 2)]
                continue
            seed_ranges = [(seed, seed + 1) for seed in seeds]
        elif not line and map_name:
            seed_ranges.extend(temp_ranges)
            temp_ranges = []
            map_name = ""
        elif not map_name:
            map_name = line
        else:
            vals = [int(num) for num in line.split(" ")]
            from_start = vals[1]
            from_stop = vals[1] + vals[2]
            rule = vals[0] - vals[1]
            for seed_index, seed_range in enumerate(seed_ranges):
                if from_stop > seed_range[0] and from_start < seed_range[1]:
                    if from_start > seed_range[0] and from_stop < seed_range[1]:
                        seed_ranges[seed_index] = (seed_range[0], from_start)
                        seed_ranges.append((from_stop, seed_range[1]))
                        temp_ranges.append((from_start + rule, from_stop + rule))
                    elif from_start > seed_range[0]:
                        seed_ranges[seed_index] = (seed_range[0], from_start)
                        temp_ranges.append((from_start + rule, seed_range[1] + rule))
                    elif from_stop < seed_range[1]:
                        seed_ranges[seed_index] = (from_stop, seed_range[1])
                        temp_ranges.append((seed_range[0] + rule, from_stop + rule))
                    else:
                        seed_ranges[seed_index] = False
                        temp_ranges.append((seed_range[0] + rule, seed_range[1] + rule))
            seed_ranges = [seed_range for seed_range in seed_ranges if seed_range]
    seed_ranges.extend(temp_ranges)

    locations = []
    for seed_range in seed_ranges:
        locations.append(seed_range[0])

    return min(locations)
