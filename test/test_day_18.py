import unittest

from aocd import get_data

from src.day_18 import DigPlan, part_x


def get_example(use_colour=False):
    lines = [
        "R 6 (#70c710)",
        "D 5 (#0dc571)",
        "L 2 (#5713f0)",
        "D 2 (#d2c081)",
        "R 2 (#59c680)",
        "D 2 (#411b91)",
        "L 5 (#8ceee2)",
        "U 2 (#caa173)",
        "L 1 (#1b58a2)",
        "U 2 (#caa171)",
        "R 2 (#7807d2)",
        "U 3 (#a77fa3)",
        "L 2 (#015232)",
        "U 2 (#7a21e3)",
    ]
    dig_plans = [DigPlan.from_line(line, use_colour) for line in lines]
    return dig_plans


def get_input(use_colour=False):
    lines = get_data(day=18, year=2023).splitlines()
    dig_plans = [DigPlan.from_line(line, use_colour) for line in lines]
    return dig_plans


class TestDay18(unittest.TestCase):
    def test__part_1_example(self):
        dig_plans = get_example()
        assert part_x(dig_plans) == 62

    def test__part_1_input(self):
        dig_plans = get_input()
        print(part_x(dig_plans))

    def test__part_2_example(self):
        dig_plans = get_example(use_colour=True)
        assert part_x(dig_plans) == 952408144115

    def test__part_2_input(self):
        dig_plans = get_input(use_colour=True)
        print(part_x(dig_plans))
