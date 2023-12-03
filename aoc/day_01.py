"""Processing for Day 01"""

import re

def trebuchet(document: str, as_word: bool) -> int:
    """Take a document and return the appropriate value"""

    if as_word:
        document = (
            document
            .replace("eight", "e8t")
            .replace("one",   "o1")
            .replace("two",   "2")
            .replace("three", "3")
            .replace("four",  "4")
            .replace("five",  "5")
            .replace("six",   "6")
            .replace("nine",  "9")
            .replace("seven", "7")
        )

    document = re.sub(r"[^\d\n]", "", document)

    lines = document.splitlines()

    nums = [int(line[0] + line[-1]) for line in lines]

    return sum(nums)
