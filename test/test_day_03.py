import unittest

from aocd import get_data

from src.day_03 import part_1, part_2


def get_example():
    lines = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    return lines


def get_input():
    lines = get_data(day=3, year=2023).splitlines()
    return lines


class TestDay03(unittest.TestCase):
    def test__part_1_example(self):
        lines = get_example()
        assert part_1(lines) == 4361

    def test__part_1_input(self):
        lines = get_input()
        print(part_1(lines))

    def test__part_2_example(self):
        lines = get_example()
        assert part_2(lines) == 467835

    def test__part_2_input(self):
        lines = get_input()
        print(part_2(lines))
