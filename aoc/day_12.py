"""Processing for Day 12"""

import functools
import re

def hot_springs(records: str, folded: bool) -> int:
    """Take the records and return the appropriate value"""

    arrangements = 0

    for record in records.splitlines():
        string, groups = record.split(" ")
        if folded:
            string = "?".join([string] * 5)
            groups = ",".join([groups] * 5)

        string = re.sub(r"\.+", ".", string.strip("."))
        strings = string.split(".")

        groups_list = [int(g) for g in groups.split(",")]

        arrangements += _check_next(tuple(strings[::-1]), tuple(groups_list[::-1]))

    return arrangements


@functools.lru_cache(maxsize=512)
def _check_next(strings: tuple[str, ...], groups: tuple[int, ...]) -> int:
    """Function to recurse with"""

    if not groups:
        if strings and any(("#" in g for g in strings)):
            # this is not a solution
            return 0
        # this is a solution
        return 1
    if not strings:
        # this is not a solution
        return 0

    possibilities = 0

    string = strings[-1]
    strings = strings[:-1]

    # there is a possibility this string isn't used at all
    if strings and "#" not in string:
        # consume the first string, consume no groups
        possibilities += _check_next(strings, groups)

    group = groups[-1]
    groups = groups[:-1]

    while len(string) >= group:
        if len(string) == group:
            possibilities += _check_next(strings, groups)
        elif len(string) == (group + 1) and string[group] == "?":
            temp = _check_next(strings, groups)
            if string[0] == "?":
                possibilities += 2 * temp
                break
            possibilities += temp
        elif string[group] == "?":
            possibilities += _check_next(tuple(list(strings) + [string[group+1:]]), groups)
        if string[0] == "#":
            break
        string = string[1:]

    return possibilities
