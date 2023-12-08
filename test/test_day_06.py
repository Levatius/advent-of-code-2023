import unittest

from aocd import get_data

from src.day_06 import get_races, part_x


def get_example(part):
    lines = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]
    races = get_races(lines, part)
    return races


def get_input(part):
    lines = get_data(day=6, year=2023).splitlines()
    races = get_races(lines, part)
    return races


class TestDay06(unittest.TestCase):
    def test__part_1_example(self):
        races = get_example(part=1)
        assert part_x(races) == 288

    def test__part_1_input(self):
        races = get_input(part=1)
        print(part_x(races))

    def test__part_2_example(self):
        races = get_example(part=2)
        assert part_x(races) == 71503

    def test__part_2_input(self):
        races = get_input(part=2)
        print(part_x(races))
