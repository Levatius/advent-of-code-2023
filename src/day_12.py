from functools import lru_cache

from more_itertools import windowed


def get_records(lines, folds):
    spring_records = []
    group_records = []
    for line in lines:
        springs, groups = line.split(" ")
        springs = "?".join(springs for _ in range(folds))
        spring_records.append(springs)
        groups = tuple(int(group) for group in groups.split(","))
        groups *= folds
        group_records.append(groups)
    return zip(spring_records, group_records)


@lru_cache
def get_next_springs(springs, group_size):
    next_springs_list = []
    for start, sub_springs in enumerate(windowed(springs, group_size)):
        if None in sub_springs or "#" in springs[:start]:
            # Unrecoverable states, break
            break
        end = start + group_size
        next_springs = springs[end:]
        if "." in sub_springs or (next_springs and next_springs[0] == "#"):
            # Recoverable states, continue
            continue
        next_springs_list.append(next_springs[1:])
    return next_springs_list


@lru_cache
def calc_combinations(springs, groups):
    total = 0
    for next_springs in get_next_springs(springs, groups[0]):
        if next_groups := groups[1:]:
            # Move onto the next groups
            total += calc_combinations(next_springs, next_groups)
        elif "#" not in next_springs:
            # If we still have broken springs remaining, our match has failed
            total += 1
    return total


def part_x(records):
    return sum(calc_combinations(springs, groups) for springs, groups in records)
