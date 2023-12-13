import unittest

from aocd import get_data

from src.day_13 import get_patterns, part_x


def get_example():
    lines = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
        "",
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]
    patterns = get_patterns(lines)
    return patterns


def get_input():
    lines = get_data(day=13, year=2023).splitlines()
    patterns = get_patterns(lines)
    return patterns


class TestDay13(unittest.TestCase):
    def test__part_1_example(self):
        patterns = get_example()
        assert part_x(patterns, target_reflective_error=0) == 405

    def test__part_1_input(self):
        patterns = get_input()
        print(part_x(patterns, target_reflective_error=0))

    def test__part_2_example(self):
        patterns = get_example()
        assert part_x(patterns, target_reflective_error=1) == 400

    def test__part_2_input(self):
        patterns = get_input()
        print(part_x(patterns, target_reflective_error=1))
