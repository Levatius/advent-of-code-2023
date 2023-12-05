from dataclasses import dataclass, field

import portion as p
from more_itertools import chunked


@dataclass
class Mapping:
    source: p.closedopen
    destination: p.closedopen

    @classmethod
    def from_data(cls, destination_start, source_start, length):
        source = p.closedopen(source_start, source_start + length)
        destination = p.closedopen(destination_start, destination_start + length)
        return Mapping(source, destination)

    def transform_number(self, number):
        return number - self.source.lower + self.destination.lower

    def transform_interval(self, interval):
        mappable_interval = interval & self.source
        unmappable_interval = interval - self.source
        mapped_interval = p.closedopen(
            lower=mappable_interval.lower - self.source.lower + self.destination.lower,
            upper=mappable_interval.upper - self.source.upper + self.destination.upper
        )
        return mapped_interval, unmappable_interval


@dataclass
class Map:
    name: str
    mappings: list[Mapping] = field(default_factory=list)

    def transform_number(self, number):
        for mapping in self.mappings:
            if number in mapping.source:
                return mapping.transform_number(number)
        return number

    def transform_interval(self, interval):
        transformed_interval = p.empty()
        remaining_interval = p.closedopen(interval.lower, interval.upper)

        for mapping in self.mappings:
            if (interval & mapping.source).empty:
                continue
            mapped_interval, unmappable_interval = mapping.transform_interval(interval)
            transformed_interval |= mapped_interval
            remaining_interval &= unmappable_interval

        return transformed_interval | remaining_interval


def get_seeds_and_maps(lines, part):
    seeds = [int(number) for number in lines[0].split(": ")[1].split(" ")]
    # Convert seed numbers to seed intervals for Part 2
    if part == 2:
        seeds = [p.closedopen(start, start + length) for start, length in chunked(seeds, 2)]

    maps = []
    for line in lines[1:]:
        # Skip empty line
        if not line:
            continue
        # Create a new Map when a map name is found
        if line.endswith("map:"):
            map_ = Map(name=line.split(" ")[0])
            maps.append(map_)
            continue
        # Add Mappings to the last added Map
        destination_start, source_start, length = (int(item) for item in line.split(" "))
        mapping = Mapping.from_data(destination_start, source_start, length)
        maps[-1].mappings.append(mapping)

    return seeds, maps


def part_1(seeds, maps):
    numbers = seeds
    for map_ in maps:
        numbers = [map_.transform_number(number) for number in numbers]
    return min(numbers)


def part_2(seeds, maps):
    intervals = seeds
    for map_ in maps:
        intervals = [map_.transform_interval(interval) for interval in intervals]
    return min(intervals, key=lambda item: item.lower).lower
