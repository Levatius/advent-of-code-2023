import unittest

from aocd import get_data

from src.day_11 import part_x


def get_example():
    starmap = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]
    return starmap


def get_input():
    starmap = get_data(day=11, year=2023).splitlines()
    return starmap


class TestDay11(unittest.TestCase):
    def test__part_1_example(self):
        starmap = get_example()
        assert part_x(starmap, age=2) == 374

    def test__part_1_input(self):
        starmap = get_input()
        print(part_x(starmap, age=2))

    def test__part_2_example_1(self):
        starmap = get_example()
        assert part_x(starmap, age=10) == 1030

    def test__part_2_example_2(self):
        starmap = get_example()
        assert part_x(starmap, age=100) == 8410

    def test__part_2_input(self):
        starmap = get_input()
        print(part_x(starmap, age=1_000_000))
