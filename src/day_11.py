import itertools

from numpy import array, linalg


def get_galaxies(starmap):
    galaxies = set()
    for j, line in enumerate(starmap):
        for i, item in enumerate(line):
            if item == "#":
                galaxies.add((i, j))
    return galaxies


def expand_galaxies(galaxies, age):
    expanded_galaxies = set()
    dimensions = (0, 1)
    populated = [{galaxy[i] for galaxy in galaxies} for i in dimensions]
    for galaxy in galaxies:
        expanded_pos = []
        for i in dimensions:
            pos_i = galaxy[i]
            delta_i = pos_i - sum(1 for pop_i in populated[i] if pop_i < pos_i)
            expanded_pos_i = pos_i + (age - 1) * delta_i
            expanded_pos.append(expanded_pos_i)
        expanded_galaxies.add(tuple(expanded_pos))
    return expanded_galaxies


def part_x(starmap, age):
    galaxies = get_galaxies(starmap)
    expanded_galaxies = expand_galaxies(galaxies, age)

    total = 0
    for galaxy_a, galaxy_b in itertools.combinations(expanded_galaxies, 2):
        distance = linalg.norm(array(galaxy_b) - array(galaxy_a), ord=1)
        total += int(distance)
    return total
