import unittest

from aocd import get_data

from src.day_08 import get_instructions_and_nodes, part_1, part_2


def get_example_1():
    lines = [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    instructions, nodes = get_instructions_and_nodes(lines)
    return instructions, nodes


def get_example_2():
    lines = [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    instructions, nodes = get_instructions_and_nodes(lines)
    return instructions, nodes


def get_example_3():
    lines = [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]
    instructions, nodes = get_instructions_and_nodes(lines)
    return instructions, nodes


def get_input():
    lines = get_data(day=8, year=2023).splitlines()
    instructions, nodes = get_instructions_and_nodes(lines)
    return instructions, nodes


class TestDay08(unittest.TestCase):
    def test__part_1_example_1(self):
        instructions, nodes = get_example_1()
        assert part_1(instructions, nodes) == 2

    def test__part_1_example_2(self):
        instructions, nodes = get_example_2()
        assert part_1(instructions, nodes) == 6

    def test__part_1_input(self):
        instructions, nodes = get_input()
        print(part_1(instructions, nodes))

    def test__part_2_example_3(self):
        instructions, nodes = get_example_3()
        assert part_2(instructions, nodes) == 6

    def test__part_2_input(self):
        instructions, nodes = get_input()
        print(part_2(instructions, nodes))
