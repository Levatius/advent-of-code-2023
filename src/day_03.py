import itertools
import re
from dataclasses import dataclass

from numpy import array, array_equal, linalg


@dataclass
class Part:
    number: int
    positions: list[array]

    def is_valid(self, gizmos):
        for gizmo in gizmos:
            if check_adjacent(self, gizmo):
                return True
        return False


class Gizmo:
    symbol: str
    position: array
    boundary_positions: list[array]

    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position
        self.boundary_positions = self._get_boundary_positions()

    @property
    def is_gear(self):
        return self.symbol == "*"

    def _get_boundary_positions(self):
        boundary_offsets = [[array([i, j]) for i in (-1, 0, 1) if not (i == 0 and j == 0)] for j in (-1, 0, 1)]
        boundary_offsets = itertools.chain.from_iterable(boundary_offsets)
        boundary_positions = [self.position + offset for offset in boundary_offsets]
        return boundary_positions

    def get_adjacent_parts(self, parts):
        adjacent_parts = [part for part in parts if check_adjacent(part, self)]
        return adjacent_parts


def get_parts_and_gizmos(lines):
    parts, gizmos = [], []
    for j, line in enumerate(lines):
        # Parts
        items = re.finditer(r"(\d+)", line)
        for item in items:
            part = Part(
                number=int(item.group()),
                positions=[array([i, j]) for i in range(item.start(), item.end())]
            )
            parts.append(part)
        # Gizmos
        items = re.finditer(r"([^\d.])", line)
        for item in items:
            gizmo = Gizmo(
                symbol=item.group(),
                position=array([item.start(), j])
            )
            gizmos.append(gizmo)
    return parts, gizmos


def check_adjacent(part, gizmo, part_number_max_digits=3):
    # Returns False quickly when far apart, assumes part numbers have a max of 3 digits
    if linalg.norm(part.positions[0] - gizmo.position, ord=1) > part_number_max_digits + 1:
        return False
    # Otherwise, check thoroughly for adjacency
    for position in part.positions:
        for boundary_position in gizmo.boundary_positions:
            if array_equal(position, boundary_position):
                return True
    return False


def part_1(lines):
    parts, gizmos = get_parts_and_gizmos(lines)
    total = 0
    for part in parts:
        if part.is_valid(gizmos):
            total += part.number
    return total


def part_2(lines):
    parts, gizmos = get_parts_and_gizmos(lines)
    total = 0
    for gizmo in gizmos:
        if not gizmo.is_gear:
            continue
        if len(adjacent_parts := gizmo.get_adjacent_parts(parts)) == 2:
            total += adjacent_parts[0].number * adjacent_parts[1].number
    return total
