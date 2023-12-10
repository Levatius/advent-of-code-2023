import unittest

from aocd import get_data

from src.day_10 import get_graph, part_1, part_2


def get_example_1():
    lines = [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ]
    graph = get_graph(lines)
    return graph


def get_example_2():
    lines = [
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    ]
    graph = get_graph(lines)
    return graph


def get_example_3():
    lines = [
        "...........",
        ".S-------7.",
        ".|F-7.F-7|.",
        ".||.L-J.||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "...........",
    ]
    graph = get_graph(lines)
    return graph


def get_example_4():
    lines = [
        "..........",
        ".S------7.",
        ".|F----7|.",
        ".||....||.",
        ".||....||.",
        ".|L-7F-J|.",
        ".|..||..|.",
        ".L--JL--J.",
        "..........",
    ]
    graph = get_graph(lines)
    return graph


def get_example_5():
    lines = [
        "FF7FSF7F7F7F7F7F---7",
        "L|LJ||||||||||||F--J",
        "FL-7LJLJ||||||LJL-77",
        "F--JF--7||LJLJ7F7FJ-",
        "L---JF-JLJ.||-FJLJJ7",
        "|F|F-JF---7F7-L7L|7|",
        "|FFJF7L7F-JF7|JL---7",
        "7-L-JL7||F7|L7F-7F7|",
        "L.L7LFJ|||||FJL7||LJ",
        "L7JLJL-JLJLJL--JLJ.L",
    ]
    graph = get_graph(lines)
    return graph


def get_input():
    lines = get_data(day=10, year=2023).splitlines()
    graph = get_graph(lines)
    return graph


class TestDay10(unittest.TestCase):
    def test__part_1_example_1(self):
        graph = get_example_1()
        assert part_1(graph) == 4

    def test__part_1_example_2(self):
        graph = get_example_2()
        assert part_1(graph) == 8

    def test__part_1_input(self):
        graph = get_input()
        print(part_1(graph))

    def test__part_2_example_1(self):
        graph = get_example_1()
        assert part_2(graph) == 1

    def test__part_2_example_2(self):
        graph = get_example_2()
        assert part_2(graph) == 1

    def test__part_2_example_3(self):
        graph = get_example_3()
        assert part_2(graph) == 5

    def test__part_2_example_4(self):
        graph = get_example_4()
        assert part_2(graph) == 4

    def test__part_2_example_5(self):
        graph = get_example_5()
        assert part_2(graph) == 10

    def test__part_2_input(self):
        graph = get_input()
        print(part_2(graph))
