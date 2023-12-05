import unittest

from aocd import get_data

from src.day_05 import get_seeds_and_maps, part_1, part_2


def get_example(part):
    lines = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]
    seeds, maps = get_seeds_and_maps(lines, part)
    return seeds, maps


def get_input(part):
    lines = get_data(day=5, year=2023).splitlines()
    seeds, maps = get_seeds_and_maps(lines, part)
    return seeds, maps


class TestDay05(unittest.TestCase):
    def test__part_1_example(self):
        seeds, maps = get_example(part=1)
        assert part_1(seeds, maps) == 35

    def test__part_1_input(self):
        seeds, maps = get_input(part=1)
        print(part_1(seeds, maps))

    def test__part_2_example(self):
        seeds, maps = get_example(part=2)
        assert part_2(seeds, maps) == 46

    def test__part_2_input(self):
        seeds, maps = get_input(part=2)
        print(part_2(seeds, maps))
