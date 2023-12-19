import operator
import re
from collections import defaultdict
from dataclasses import dataclass

import portion as p


@dataclass
class Rule:
    category: str
    operator: operator
    value: int
    destination: str

    @classmethod
    def from_line(cls, line):
        m = re.match(r"(?P<category>\w)(?P<operator>[><])(?P<value>\d+):(?P<destination>\w+)", line)
        valid_operators = {">": operator.gt, "<": operator.lt}
        return cls(
            category=m.group("category"),
            operator=valid_operators[m.group("operator")],
            value=int(m.group("value")),
            destination=m.group("destination")
        )


@dataclass
class Workflow:
    name: str
    rules: list[Rule]
    default_destination: str

    @classmethod
    def from_line(cls, line):
        m = re.match(r"(?P<name>\w+)\{(?P<rules>.+),(?P<default_destination>\w+)}", line)
        rules = [Rule.from_line(rule) for rule in m.group("rules").split(",")]
        return cls(m.group("name"), rules, m.group("default_destination"))


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    @classmethod
    def from_line(cls, line):
        m = re.match(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line)
        values = [int(value) for value in m.groups()]
        return cls(*values)

    @property
    def rating(self):
        return self.x + self.m + self.a + self.s


@dataclass
class IntervalPart:
    x: p.interval = p.closed(1, 4000)
    m: p.interval = p.closed(1, 4000)
    a: p.interval = p.closed(1, 4000)
    s: p.interval = p.closed(1, 4000)

    @property
    def combinations(self):
        def length(i):
            return (i.upper if i.right is p.CLOSED else i.upper - 1) - (i.lower - 1 if i.left is p.CLOSED else i.lower)

        return length(self.x) * length(self.m) * length(self.a) * length(self.s)


def get_workflows_and_parts(lines):
    workflows = {}
    parts = []
    for line in lines:
        if not line:
            continue
        if line.startswith("{"):
            parts.append(Part.from_line(line))
        else:
            workflow = Workflow.from_line(line)
            workflows[workflow.name] = workflow
    return workflows, parts


def part_1(workflows, parts):
    total = 0
    for part in parts:
        workflow_name = "in"
        while workflow_name not in ("R", "A"):
            workflow = workflows[workflow_name]
            for rule in workflow.rules:
                if rule.operator(getattr(part, rule.category), rule.value):
                    workflow_name = rule.destination
                    break
            else:
                workflow_name = workflow.default_destination
        if workflow_name == "A":
            total += part.rating
    return total


def func(part, workflow, workflows):
    total = 0
    current_part = IntervalPart(x=part.x, m=part.m, a=part.a, s=part.s)
    for rule in workflow.rules:
        new_part = IntervalPart(x=current_part.x, m=current_part.m, a=current_part.a, s=current_part.s)
        match rule.operator:
            case operator.gt:
                interval = p.openclosed(rule.value, 4000)
                setattr(new_part, rule.category, getattr(new_part, rule.category).intersection(interval))
                interval = p.closed(1, rule.value)
                setattr(current_part, rule.category, getattr(current_part, rule.category).intersection(interval))
            case operator.lt:
                interval = p.closedopen(1, rule.value)
                setattr(new_part, rule.category, getattr(new_part, rule.category).intersection(interval))
                interval = p.closed(rule.value, 4000)
                setattr(current_part, rule.category, getattr(current_part, rule.category).intersection(interval))
        if rule.destination not in ("A", "R"):
            total += func(new_part, workflows[rule.destination], workflows)
        elif rule.destination == "A":
            total += new_part.combinations
    if workflow.default_destination not in ("A", "R"):
        total += func(current_part, workflows[workflow.default_destination], workflows)
    elif workflow.default_destination == "A":
        total += current_part.combinations
    return total


def part_2(workflows):
    total = func(IntervalPart(), workflows["in"], workflows)
    return total
