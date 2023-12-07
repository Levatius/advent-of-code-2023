import unittest

from aocd import get_data

from src.day_07 import Hand, part_x


def get_example(part):
    lines = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    hands = [Hand.from_line(line, part) for line in lines]
    return hands


def get_input(part):
    lines = get_data(day=7, year=2023).splitlines()
    hands = [Hand.from_line(line, part) for line in lines]
    return hands


class TestDay04(unittest.TestCase):
    def test__part_1_example(self):
        hands = get_example(part=1)
        assert part_x(hands) == 6440

    def test__part_1_input(self):
        hands = get_input(part=1)
        print(part_x(hands))

    def test__part_2_example(self):
        cards = get_example(part=2)
        assert part_x(cards) == 5905

    def test__part_2_input(self):
        cards = get_input(part=2)
        print(part_x(cards))
