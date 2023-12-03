import unittest

from aocd import get_data

from src.day_02 import Game, part_1, part_2


def get_example():
    lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    games = [Game.from_line(line) for line in lines]
    return games


def get_input():
    lines = get_data(day=2, year=2023).splitlines()
    games = [Game.from_line(line) for line in lines]
    return games


class TestDay02(unittest.TestCase):
    def test__part_1_example(self):
        games = get_example()
        assert part_1(games) == 8

    def test__part_1_input(self):
        games = get_input()
        print(part_1(games))

    def test__part_2_example(self):
        games = get_example()
        assert part_2(games) == 2286

    def test__part_2_input(self):
        games = get_input()
        print(part_2(games))
