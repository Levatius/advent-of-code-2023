import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Lens:
    label: str
    focal_length: int

    def __eq__(self, label):
        return self.label == label


def calc_hash(chars):
    current_value = 0
    for char in chars:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part_1(steps):
    return sum(calc_hash(step) for step in steps)


def part_2(steps):
    boxes = defaultdict(list)
    for step in steps:
        label, operator, focal_length = re.split(r"([=-])", step)
        box = boxes[calc_hash(label)]
        match operator:
            case "=":
                focal_length = int(focal_length)
                if label in box:
                    lens = box[box.index(label)]
                    lens.focal_length = focal_length
                else:
                    lens = Lens(label, focal_length)
                    box.append(lens)
            case "-":
                if label in box:
                    box.remove(label)
    return sum(sum((j + 1) * i * lens.focal_length for i, lens in enumerate(box, 1)) for j, box in boxes.items())
