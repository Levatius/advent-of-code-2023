import unittest

from aocd import get_data

from src.day_09 import part_1, part_2


def get_example():
    lines = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]
    sequences = [[int(value) for value in line.split(" ")] for line in lines]
    return sequences


def get_input():
    lines = get_data(day=9, year=2023).splitlines()
    sequences = [[int(value) for value in line.split(" ")] for line in lines]
    return sequences


class TestDay09(unittest.TestCase):
    def test__part_1_example(self):
        sequences = get_example()
        assert part_1(sequences) == 114

    def test__part_1_input(self):
        sequences = get_input()
        print(part_1(sequences))

    def test__part_2_example(self):
        sequences = get_example()
        assert part_2(sequences) == 2

    def test__part_2_input(self):
        sequences = get_input()
        print(part_2(sequences))
