import unittest

from aocd import get_data

from src.day_01 import DIGIT_WORDS, part_x


def get_example_1():
    lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    return lines


def get_example_2():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    return lines


def get_input():
    lines = get_data(day=1, year=2023).splitlines()
    return lines


class TestDay01(unittest.TestCase):
    def test__part_1_example(self):
        lines = get_example_1()
        digit_words = DIGIT_WORDS.values()
        assert part_x(lines, digit_words) == 142

    def test__part_1_input(self):
        lines = get_input()
        digit_words = DIGIT_WORDS.values()
        print(part_x(lines, digit_words))

    def test__part_2_example(self):
        lines = get_example_2()
        digit_words = [*DIGIT_WORDS.keys(), *DIGIT_WORDS.values()]
        assert part_x(lines, digit_words) == 281

    def test__part_2_input(self):
        lines = get_input()
        digit_words = [*DIGIT_WORDS.keys(), *DIGIT_WORDS.values()]
        print(part_x(lines, digit_words))
