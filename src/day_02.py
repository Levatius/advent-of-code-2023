import functools
import operator
import re
from dataclasses import dataclass


@dataclass
class Game:
    id: int
    records: list[dict]

    @classmethod
    def from_line(cls, line):
        match = re.match(r"Game (?P<id>\d+): (?P<records>.+)", line)

        game_id = int(match.group("id"))

        records = []
        for record in match.group("records").split("; "):
            cubes = {}
            for cube in record.split(", "):
                match = re.match(r"(?P<count>\d+) (?P<colour>\w+)", cube)
                colour, count = match.group("colour"), int(match.group("count"))
                cubes[colour] = count
            records.append(cubes)

        return cls(game_id, records)

    def is_possible_with(self, cubes):
        for record in self.records:
            for colour, count in record.items():
                if cubes[colour] < count:
                    return False
        return True

    def get_power(self):
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for record in self.records:
            for colour, count in record.items():
                if min_cubes[colour] < count:
                    min_cubes[colour] = count
        power = functools.reduce(operator.mul, min_cubes.values(), 1)
        return power


def part_1(games):
    total = 0
    for game in games:
        if game.is_possible_with(cubes={"red": 12, "green": 13, "blue": 14}):
            total += game.id
    return total


def part_2(games):
    total = 0
    for game in games:
        total += game.get_power()
    return total
