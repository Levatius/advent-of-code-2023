from functools import lru_cache

import regex


def get_records(lines, folds):
    spring_records = []
    condition_records = []
    for line in lines:
        springs, conditions = line.split(" ")
        # Springs
        springs = "?".join(springs for _ in range(folds))
        spring_records.append(springs)
        # Conditions
        conditions = [int(condition) for condition in conditions.split(",")]
        conditions *= folds
        condition_records.append(conditions)
    return zip(spring_records, tuple(condition_records))


@lru_cache
def calc_combinations(springs, conditions):
    total = 0
    for match in regex.finditer(fr"([#?]{{{conditions[0]}}})", springs, overlapped=True):
        i, j = match.regs[1]
        skipped_springs, next_springs = springs[:i], springs[j:]
        if "#" in skipped_springs or (len(next_springs) and next_springs[0] == "#"):
            continue
        if next_conditions := conditions[1:]:
            total += calc_combinations(next_springs[1:], next_conditions)
        elif "#" not in next_springs:
            total += 1
    return total


def part_x(records):
    total = 0
    for spring_records, condition_records in records:
        total += calc_combinations(spring_records, tuple(condition_records))
    return total
