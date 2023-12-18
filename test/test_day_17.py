import unittest

from aocd import get_data

from numpy import array
from src.day_17 import part_x


def get_example_1():
    lines = [
        "2413432311323",
        "3215453535623",
        "3255245654254",
        "3446585845452",
        "4546657867536",
        "1438598798454",
        "4457876987766",
        "3637877979653",
        "4654967986887",
        "4564679986453",
        "1224686865563",
        "2546548887735",
        "4322674655533",
    ]
    heatmap = array([[int(heat_loss) for heat_loss in line] for line in lines])
    return heatmap


def get_example_2():
    lines = [
        "111111111111",
        "999999999991",
        "999999999991",
        "999999999991",
        "999999999991",
    ]
    heatmap = array([[int(heat_loss) for heat_loss in line] for line in lines])
    return heatmap


def get_input():
    lines = get_data(day=17, year=2023).splitlines()
    heatmap = array([[int(heat_loss) for heat_loss in line] for line in lines])
    return heatmap


class TestDay17(unittest.TestCase):
    def test__part_1_example_1(self):
        heatmap = get_example_1()
        assert part_x(heatmap) == 102

    def test__part_1_input(self):
        heatmap = get_input()
        print(part_x(heatmap))

    def test__part_2_example_1(self):
        heatmap = get_example_1()
        assert part_x(heatmap, min_range=4, max_range=10) == 94

    def test__part_2_example_2(self):
        heatmap = get_example_2()
        assert part_x(heatmap, min_range=4, max_range=10) == 71

    def test__part_2_input(self):
        heatmap = get_input()
        print(part_x(heatmap, min_range=4, max_range=10))
