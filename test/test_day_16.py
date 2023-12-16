import unittest

from aocd import get_data

from numpy import array
from src.day_16 import Tile, part_1, part_2


def get_example():
    lines = [
        ".|...\\....",
        "|.-.\\.....",
        ".....|-...",
        "........|.",
        "..........",
        ".........\\",
        "..../.\\\\..",
        ".-.-/..|..",
        ".|....-|.\\",
        "..//.|....",
    ]
    tiles = array([[Tile(symbol) for symbol in line] for line in lines])
    return tiles


def get_input():
    lines = get_data(day=16, year=2023).splitlines()
    tiles = array([[Tile(symbol) for symbol in line] for line in lines])
    return tiles


class TestDay16(unittest.TestCase):
    def test__part_1_example(self):
        tiles = get_example()
        assert part_1(tiles) == 46

    def test__part_1_input(self):
        tiles = get_input()
        print(part_1(tiles))

    def test__part_2_example(self):
        tiles = get_example()
        assert part_2(tiles) == 51

    def test__part_2_input(self):
        tiles = get_input()
        print(part_2(tiles))
