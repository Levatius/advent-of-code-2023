import functools
import operator
import re
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
        # Example line: "a<2006:qkq"
        valid_operators = {">": operator.gt, "<": operator.lt}
        m = re.match(fr"(?P<category>\w)(?P<operator>[><])(?P<value>\d+):(?P<destination>\w+)", line)
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
        # Example line: "px{a<2006:qkq,m>2090:A,rfg}"
        m = re.match(r"(?P<name>\w+)\{(?P<rules>.+),(?P<default_destination>\w+)}", line)
        rules = [Rule.from_line(rule) for rule in m.group("rules").split(",")]
        return cls(m.group("name"), rules, m.group("default_destination"))


def get_workflows_and_parts(lines):
    workflows = {}
    parts = []
    for line in lines:
        if not line:
            continue
        if line.startswith("{"):
            part = {category: int(value) for category, value in re.findall(r"(\w)=(\d+)", line)}
            parts.append(part)
        else:
            workflow = Workflow.from_line(line)
            workflows[workflow.name] = workflow
    return workflows, parts


def part_1(workflows, parts):
    total = 0
    for part in parts:
        workflow_name = "in"
        # Zoom through workflows until we reach either the accepted (A) or rejected (R) destinations
        while workflow_name not in ("A", "R"):
            workflow = workflows[workflow_name]
            for rule in workflow.rules:
                if rule.operator(part[rule.category], rule.value):
                    workflow_name = rule.destination
                    break
            else:
                workflow_name = workflow.default_destination
        total += sum(part.values()) if workflow_name == "A" else 0
    return total


def combinations(part_range):
    # Why is length not in the portion library?
    def length(i):
        return (i.upper if i.right is p.CLOSED else i.upper - 1) - (i.lower - 1 if i.left is p.CLOSED else i.lower)

    return functools.reduce(operator.mul, (length(interval) for interval in part_range.values()), 1)


def part_2(workflows, part_range, workflow_name="in"):
    # Handle accepted (A) and rejected (R) destinations
    match workflow_name:
        case "A":
            return combinations(part_range)
        case "R":
            return 0

    total = 0
    current_part_range = dict(part_range)
    workflow = workflows[workflow_name]

    for rule in workflow.rules:
        new_part_range = dict(current_part_range)
        match rule.operator:
            case operator.gt:
                new_part_range[rule.category] &= p.openclosed(rule.value, 4000)
                current_part_range[rule.category] &= p.closed(1, rule.value)
            case operator.lt:
                new_part_range[rule.category] &= p.closedopen(1, rule.value)
                current_part_range[rule.category] &= p.closed(rule.value, 4000)
        # The new part range goes to the rule's destination
        total += part_2(workflows, new_part_range, rule.destination)
    # The remaining part range goes to the workflow's default destination
    total += part_2(workflows, current_part_range, workflow.default_destination)
    return total
