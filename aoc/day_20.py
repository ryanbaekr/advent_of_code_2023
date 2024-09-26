"""Processing for Day 20"""

from math import lcm

def pulse_propagation(configuration: str, product: bool) -> int:
    """Take the configuration and return the appropriate value"""

    if product:
        return _propagate(configuration, product)

    # visual inspection shows that the network can be broken into 4 independent subnets
    # rx is ultimately brought low when all 4 subnets output low
    # result is the LCM of the presses needed to bring each subnet low
    subconfig_1 = "broadcaster -> pj\n%pj -> zj, zq\n%zj -> cf\n%cf -> gr, zq\n%gr -> ln\n%ln -> rm\n%rm -> zq, fs\n%fs -> ff\n%ff -> cl\n%cl -> fp, zq\n%fp -> rd, zq\n%rd -> nc, zq\n%nc -> zq\n&zq -> fs, gr, ff, ln, zj, pj, rx\n"
    subconfig_2 = "broadcaster -> fg\n%fg -> nt, gt\n%gt -> jc\n%jc -> nt, nk\n%nk -> rq, nt\n%rq -> ft\n%ft -> fh\n%fh -> nt, xz\n%xz -> dr\n%dr -> xd, nt\n%xd -> nt, lm\n%lm -> nt, qn\n%qn -> nt\n&nt -> rq, fg, ft, gt, xz, rx\n"
    subconfig_3 = "broadcaster -> bh\n%bh -> qd, vv\n%qd -> xb\n%xb -> bl, vv\n%bl -> bb\n%bb -> nb, vv\n%nb -> dv\n%dv -> vv, hr\n%hr -> dm, vv\n%dm -> kg\n%kg -> mr, vv\n%mr -> vv, pz\n%pz -> vv\n&vv -> dm, bl, nb, qd, bh, rx\n"
    subconfig_4 = "broadcaster -> br\n%br -> vn, jz\n%jz -> qs\n%qs -> vn, ps\n%ps -> xm\n%xm -> vn, ht\n%ht -> pp\n%pp -> mq\n%mq -> vn, zc\n%zc -> zv\n%zv -> dc, vn\n%dc -> mg, vn\n%mg -> vn\n&vn -> br, jz, ht, ps, zc, pp, rx\n"
    subconfigs = [subconfig_1, subconfig_2, subconfig_3, subconfig_4]
    subpresses = []
    for subconfig in subconfigs:
        subpresses.append(_propagate(subconfig, product))
    return lcm(*subpresses)

def _propagate(configuration: str, product: bool) -> int:
    """Process the button presses and return either the product or the number of presses"""

    modules = {}
    sources: dict[str, list[str]] = {}

    for config in configuration.splitlines():
        type_name, destinations = config.split(" -> ")
        name = type_name[1:]
        parsed_destinations = destinations.split(", ")

        for dest in parsed_destinations:
            try:
                sources[dest].append(name)
            except KeyError:
                sources[dest] = [name]

        modules[name] = {
            "type": type_name[0],
            "dest": parsed_destinations,
        }

    presses = 0
    low_pulses = 0
    high_pulses = 0

    state: dict[str, bool] = {}

    while True:
        if product and presses == 1000:
            return low_pulses * high_pulses

        presses += 1
        low_pulses += 1

        queue = ["roadcaster"]
        trigger: dict[str, list[str]] = {}

        while queue:
            next_state = state.copy()
            next_queue: list[str] = []
            next_trigger: dict[str, list[str]] = {}

            for module_name in queue:
                if module_name not in modules:
                    if not product and module_name == "rx" and any((not state[source_name] for source_name in trigger["rx"])):
                        return presses
                    continue

                module_type = modules[module_name]["type"]
                module_dest = modules[module_name]["dest"]

                dest_len = len(module_dest)

                if module_type == "%":
                    for source_name in trigger[module_name]:
                        if not state[source_name]:
                            next_queue.extend(module_dest)
                            next_state[module_name] = not next_state.get(module_name, False)
                            break
                    else:
                        continue
                elif module_type == "&":
                    next_queue.extend(module_dest)
                    for source_name in sources[module_name]:
                        if not state.get(source_name, False):
                            next_state[module_name] = True
                            break
                    else:
                        next_state[module_name] = False
                    dest_len *= len(trigger[module_name])
                else:  # broadcaster
                    next_queue.extend(module_dest)
                    next_state[module_name] = False

                low_pulses += (not next_state[module_name]) * dest_len
                high_pulses += next_state[module_name] * dest_len

                for dest in module_dest:
                    try:
                        next_trigger[dest].append(module_name)
                    except KeyError:
                        next_trigger[dest] = [module_name]

            state = next_state
            queue = list(set(next_queue))
            trigger = next_trigger
