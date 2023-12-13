import unittest

from aocd import get_data

from src.day_12 import get_records, part_x


def get_example(folds):
    lines = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]
    records = get_records(lines, folds)
    return records


def get_input(folds):
    lines = get_data(day=12, year=2023).splitlines()
    records = get_records(lines, folds)
    return records


class TestDay12(unittest.TestCase):
    def test__part_1_example(self):
        records = get_example(folds=1)
        assert part_x(records) == 21

    def test__part_1_input(self):
        records = get_input(folds=1)
        print(part_x(records))

    def test__part_2_example(self):
        records = get_example(folds=5)
        assert part_x(records) == 525152

    def test__part_2_input(self):
        records = get_input(folds=5)
        print(part_x(records))
