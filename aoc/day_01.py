"""Processing for Day 01"""

import re

def trebuchet(document: str, as_word: bool) -> int:
    """Take a document and return the appriate value"""

    if as_word:
        document = (
            document
            .replace("one",   "one1one")
            .replace("two",   "two2two")
            .replace("three", "three3three")
            .replace("four",  "four4four")
            .replace("five",  "five5five")
            .replace("six",   "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine",  "nine9nine")
        )

    document = re.sub(r"[^\d\n]", "", document)

    lines = document.splitlines()

    nums = [int(line[0] + line[-1]) for line in lines]

    return sum(nums)
