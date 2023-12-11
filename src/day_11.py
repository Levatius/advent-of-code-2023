import itertools

from numpy import array
from numpy.linalg import norm


def get_galaxies(starmap):
    galaxies = set()
    for j, line in enumerate(starmap):
        for i, item in enumerate(line):
            if item == "#":
                galaxies.add((i, j))
    return galaxies


def get_expansion_rate(galaxies):
    expansion_rate = 0
    for i in (0, 1):
        populated = {galaxy[i] for galaxy in galaxies}
        voids = {k for k in range(min(populated), max(populated) + 1)} - populated
        for void in voids:
            less_than_void = sum(1 for galaxy in galaxies if galaxy[i] < void)
            greater_than_void = sum(1 for galaxy in galaxies if galaxy[i] > void)
            expansion_rate += less_than_void * greater_than_void
    return expansion_rate


def part_x(starmap, age):
    galaxies = get_galaxies(starmap)
    base_distance = sum(int(norm(array(b) - array(a), ord=1)) for a, b in itertools.combinations(galaxies, 2))
    expansion_rate = get_expansion_rate(galaxies)
    return base_distance + (age - 1) * expansion_rate
