import functools
import operator
import re
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    record_distance: int

    def get_distance_travelled(self, charge_time):
        speed = charge_time
        return (self.time - charge_time) * speed

    def get_total_winning_races(self):
        total = 0
        for charge_time in range(1, self.time):
            distance_travelled = self.get_distance_travelled(charge_time)
            if distance_travelled > self.record_distance:
                total += 1
        return total


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
