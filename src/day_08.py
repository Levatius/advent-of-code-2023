import math
import re


def get_instructions_and_nodes(lines):
    instructions = [instruction for instruction in lines[0]]
    nodes = {}
    for line in lines[2:]:
        match = re.match(r"(?P<node>\w+) = \((?P<left_node>\w+), (?P<right_node>\w+)\)", line)
        nodes[match.group("node")] = {"L": match.group("left_node"), "R": match.group("right_node")}
    return instructions, nodes


def part_1(instructions, nodes):
    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        current_node = nodes[current_node][instruction]
        steps += 1
    return steps


def part_2(instructions, nodes):
    starting_nodes = [node for node in nodes if node.endswith("A")]
    steps = [0 for _ in starting_nodes]
    for i, current_node in enumerate(starting_nodes):
        while not current_node.endswith("Z"):
            instruction = instructions[steps[i] % len(instructions)]
            current_node = nodes[current_node][instruction]
            steps[i] += 1
    return math.lcm(*steps)
