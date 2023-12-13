from dataclasses import dataclass
from itertools import chain

from numpy import array, flip


@dataclass
class Pattern:
    rows: array

    @classmethod
    def from_lines(cls, lines):
        rows = array([list(line) for line in lines])
        return cls(rows)

    @property
    def columns(self):
        return self.rows.T

    @staticmethod
    def find_reflective_error(items, mirror_pos):
        lower_reflection = flip(items[:mirror_pos], axis=0)
        upper_reflection = items[mirror_pos:]
        # Reduce the larger reflection to the size of the smaller reflection, so we can compare them
        reflection_boundary = min(len(lower_reflection), len(upper_reflection))
        lower_reflection = lower_reflection[:reflection_boundary]
        upper_reflection = upper_reflection[:reflection_boundary]
        reflections = zip(chain.from_iterable(lower_reflection), chain.from_iterable(upper_reflection))
        # Reflective error is the total number of differences between the two reflections
        reflective_error = sum(1 for lower_item, upper_item in reflections if lower_item != upper_item)
        return reflective_error

    def calc_mirror_score(self, target_reflective_error):
        for score_multiplier, items in zip((100, 1), (self.rows, self.columns)):
            # Try the mirror position in all possible locations until we find the one that satisfies our target
            for mirror_pos in range(1, len(items)):
                reflective_error = self.find_reflective_error(items, mirror_pos)
                if reflective_error == target_reflective_error:
                    return score_multiplier * mirror_pos


def get_patterns(lines):
    lines_by_pattern = [[]]
    for line in lines:
        if not line:
            lines_by_pattern.append([])
            continue
        lines_by_pattern[-1].append(line)
    patterns = [Pattern.from_lines(pattern_lines) for pattern_lines in lines_by_pattern]
    return patterns


def part_x(patterns, target_reflective_error):
    return sum(pattern.calc_mirror_score(target_reflective_error) for pattern in patterns)
