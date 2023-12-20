import unittest

from aocd import get_data

from src.day_20 import get_modules, part_1, part_2


def get_example_1():
    lines = [
        "broadcaster -> a, b, c",
        "%a -> b",
        "%b -> c",
        "%c -> inv",
        "&inv -> a",
    ]
    modules = get_modules(lines)
    return modules


def get_example_2():
    lines = [
        "broadcaster -> a",
        "%a -> inv, con",
        "&inv -> b",
        "%b -> con",
        "&con -> output",
    ]
    modules = get_modules(lines)
    return modules


def get_input():
    lines = get_data(day=20, year=2023).splitlines()
    modules = get_modules(lines)
    return modules


class TestDay20(unittest.TestCase):
    def test__part_1_example_1(self):
        modules = get_example_1()
        assert part_1(modules) == 32000000

    def test__part_1_example_2(self):
        modules = get_example_2()
        assert part_1(modules) == 11687500

    def test__part_1_input(self):
        modules = get_input()
        print(part_1(modules))

    def test__part_2_input(self):
        modules = get_input()
        print(part_2(modules))
