"""Processing for Day 15"""

def lens_library(sequence: str, boxes: bool) -> int:
    """Take the sequence and return the appropriate value"""

    if boxes:
        box_dict = {}
        label_dict = {}

        for step in sequence.replace("\n", "").split(","):
            box = 0

            for char in step:
                if char in ["-", "="]:
                    break
                box += ord(char)
                box *= 17
                box = box % 256

            if step.endswith("-"):
                label = step[:-1]
                if label in label_dict:
                    box = label_dict[label]
                    label_dict.pop(label)
                    box_dict[box].pop(label)
            else:
                label, length = step.split("=")
                if box in box_dict:
                    box_dict[box][label] = int(length)
                else:
                    box_dict[box] = {label: int(length)}
                label_dict[label] = box

        focusing_sum = 0

        for label, box in label_dict.items():
            for slot, potential_label in enumerate(box_dict[box].keys()):
                if potential_label == label:
                    break
            focusing_pwr = 1 + box
            focusing_pwr *= 1 + slot
            focusing_pwr *= box_dict[box][label]

            focusing_sum += focusing_pwr

        return focusing_sum

    hash_sum = 0

    for step in sequence.replace("\n", "").split(","):
        step_hash = 0

        for char in step:
            step_hash += ord(char)
            step_hash *= 17
            step_hash = step_hash % 256

        hash_sum += step_hash

    return hash_sum
