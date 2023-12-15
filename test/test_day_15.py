import unittest

from aocd import get_data

from src.day_15 import part_1, part_2


def get_example():
    line = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    steps = line.split(",")
    return steps


def get_input():
    line = get_data(day=15, year=2023)
    steps = line.split(",")
    return steps


class TestDay15(unittest.TestCase):
    def test__part_1_example(self):
        steps = get_example()
        assert part_1(steps) == 1320

    def test__part_1_input(self):
        steps = get_input()
        print(part_1(steps))

    def test__part_2_example(self):
        steps = get_example()
        assert part_2(steps) == 145

    def test__part_2_input(self):
        steps = get_input()
        print(part_2(steps))
