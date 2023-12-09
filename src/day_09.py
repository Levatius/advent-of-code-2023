import itertools


def get_extrapolated_values(sequence):
    if sum(1 for value in sequence if value != 0) == 0:
        # All elements are zero, return!
        return 0, 0
    subsequence = [b - a for a, b in itertools.pairwise(sequence)]
    start_value, end_value = get_extrapolated_values(subsequence)
    return sequence[0] - start_value, sequence[-1] + end_value


def part_1(sequences):
    return sum(get_extrapolated_values(sequence)[1] for sequence in sequences)


def part_2(sequences):
    return sum(get_extrapolated_values(sequence)[0] for sequence in sequences)
