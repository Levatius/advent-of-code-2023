import unittest

from aocd import get_data

from src.day_04 import Card, part_1, part_2


def get_example():
    lines = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    cards = [Card.from_line(line) for line in lines]
    return cards


def get_input():
    lines = get_data(day=4, year=2023).splitlines()
    cards = [Card.from_line(line) for line in lines]
    return cards


class TestDay04(unittest.TestCase):
    def test__part_1_example(self):
        cards = get_example()
        assert part_1(cards) == 13

    def test__part_1_input(self):
        cards = get_input()
        print(part_1(cards))

    def test__part_2_example(self):
        cards = get_example()
        assert part_2(cards) == 30

    def test__part_2_input(self):
        cards = get_input()
        print(part_2(cards))
