import unittest

from aocd import get_data

from src.day_19 import get_workflows_and_parts, part_1, part_2


def get_example():
    lines = [
        "px{a<2006:qkq,m>2090:A,rfg}",
        "pv{a>1716:R,A}",
        "lnx{m>1548:A,A}",
        "rfg{s<537:gd,x>2440:R,A}",
        "qs{s>3448:A,lnx}",
        "qkq{x<1416:A,crn}",
        "crn{x>2662:A,R}",
        "in{s<1351:px,qqz}",
        "qqz{s>2770:qs,m<1801:hdj,R}",
        "gd{a>3333:R,R}",
        "hdj{m>838:A,pv}",
        "",
        "{x=787,m=2655,a=1222,s=2876}",
        "{x=1679,m=44,a=2067,s=496}",
        "{x=2036,m=264,a=79,s=2244}",
        "{x=2461,m=1339,a=466,s=291}",
        "{x=2127,m=1623,a=2188,s=1013}",
    ]
    workflows, parts = get_workflows_and_parts(lines)
    return workflows, parts


def get_input():
    lines = get_data(day=19, year=2023).splitlines()
    workflows, parts = get_workflows_and_parts(lines)
    return workflows, parts


class TestDay19(unittest.TestCase):
    def test__part_1_example(self):
        workflows, parts = get_example()
        assert part_1(workflows, parts) == 19114

    def test__part_1_input(self):
        workflows, parts = get_input()
        print(part_1(workflows, parts))

    def test__part_2_example(self):
        workflows, _ = get_example()
        assert part_2(workflows) == 167409079868000

    def test__part_2_input(self):
        workflows, _ = get_input()
        print(part_2(workflows))