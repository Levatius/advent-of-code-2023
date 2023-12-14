import unittest

from aocd import get_data

from numpy import array
from src.day_14 import part_1, part_2


def get_example():
    lines = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]
    dish = array([list(line) for line in lines])
    return dish


def get_input():
    lines = get_data(day=14, year=2023).splitlines()
    dish = array([list(line) for line in lines])
    return dish


class TestDay14(unittest.TestCase):
    def test__part_1_example(self):
        dish = get_example()
        assert part_1(dish) == 136

    def test__part_1_input(self):
        dish = get_input()
        print(part_1(dish))

    def test__part_2_example(self):
        dish = get_example()
        assert part_2(dish) == 64

    def test__part_2_input(self):
        dish = get_input()
        print(part_2(dish))
