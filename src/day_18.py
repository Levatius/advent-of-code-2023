import re
from dataclasses import dataclass


@dataclass
class DigPlan:
    direction: str
    length: int

    @classmethod
    def from_line(cls, line, use_colour):
        m = re.match(r"(?P<direction>\w) (?P<length>\d+) \(#(?P<colour>.{6})\)", line)
        direction = m.group("direction")
        length = int(m.group("length"))
        if use_colour:
            direction_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
            colour = m.group("colour")
            direction = direction_map[colour[-1]]
            length = int(colour[:5], 16)
        return cls(direction, length)


def part_x(dig_plans):
    total = 1
    digger_width = 1
    for dig_plan in dig_plans:
        match dig_plan.direction:
            case "R":
                total += dig_plan.length
                digger_width += dig_plan.length
            case "D":
                total += dig_plan.length * digger_width
            case "L":
                digger_width -= dig_plan.length
            case "U":
                total -= dig_plan.length * (digger_width - 1)
    return total
