import functools
import math
import operator
import re
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    record_distance: int

    def get_total_winning_races(self):
        # Quadratic formula to solve (time - charge_time) * charge_time - record_distance > 0
        numerators = [self.time - i * math.sqrt(self.time ** 2 - 4 * self.record_distance) for i in (1, -1)]
        lower_bound = math.floor(numerators[0] / 2)
        upper_bound = math.ceil(numerators[1] / 2)
        return upper_bound - lower_bound - 1


def get_races(lines, part):
    if part == 1:
        times = [int(time) for time in re.findall(r"\d+", lines[0])]
        distances = [int(distance) for distance in re.findall(r"\d+", lines[1])]
        races = [Race(time, distance) for time, distance in zip(times, distances)]
        return races
    elif part == 2:
        time = int("".join(re.findall(r"\d+", lines[0])))
        distance = int("".join(re.findall(r"\d+", lines[1])))
        race = Race(time, distance)
        return [race]


def part_x(races):
    total_winning_races = (race.get_total_winning_races() for race in races)
    return functools.reduce(operator.mul, total_winning_races, 1)
