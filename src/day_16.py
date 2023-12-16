from dataclasses import dataclass, field
from enum import Enum
from itertools import chain
from numpy import array


class Direction(Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)


@dataclass
class Tile:
    mirror: str | None = None
    energised_from: list[tuple] = field(default_factory=list)

    @property
    def energised(self):
        return len(self.energised_from) > 0

    def redirect(self, direction):
        y, x = direction
        match self.mirror:
            case "\\":
                return [(x, y)]
            case "/":
                return [(-x, -y)]
            case "|":
                if x:
                    return [Direction.UP.value, Direction.DOWN.value]
            case "-":
                if y:
                    return [Direction.LEFT.value, Direction.RIGHT.value]
        return [direction]


@dataclass
class Beam:
    pos: tuple
    direction: tuple


def collect_energy(tiles):
    total = 0
    for tile in chain.from_iterable(tiles):
        total += int(tile.energised)
        tile.energised_from = []
    return total


def part_1(tiles, initial_beam=Beam(pos=(0, 0), direction=Direction.RIGHT.value)):
    beams = [initial_beam]
    while beams:
        beam = beams.pop()
        if not all(0 <= beam.pos[i] < tiles.shape[i] for i in (0, 1)):
            continue

        tile = tiles[beam.pos]
        if beam.direction in tile.energised_from:
            continue
        tile.energised_from.append(beam.direction)

        for redirection in tile.redirect(beam.direction):
            new_beam = Beam(pos=tuple(array(beam.pos) + array(redirection)), direction=redirection)
            beams.append(new_beam)
    return collect_energy(tiles)


def part_2(tiles):
    indexes = array([[(j, i) for i, _ in enumerate(row)] for j, row in enumerate(tiles)])

    positions = [indexes[:, 0], indexes[-1, :], indexes[:, -1], indexes[0, :]]
    directions = [Direction.RIGHT.value, Direction.UP.value, Direction.LEFT.value, Direction.DOWN.value]

    totals = []
    for positions, direction in zip(positions, directions):
        for pos in positions:
            total = part_1(tiles, initial_beam=Beam(tuple(pos), direction))
            totals.append(total)
    return max(totals)
