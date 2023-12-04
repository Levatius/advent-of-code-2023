import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Card:
    id: int
    winning_numbers: list[int]
    your_numbers: list[int]

    @classmethod
    def from_line(cls, line):
        match = re.match(r"Card\s+(?P<id>\d+): (?P<winning_numbers>[\s\d]+) \| (?P<your_numbers>[\s\d]+)", line)
        card_id = int(match.group("id"))
        winning_numbers = [int(number) for number in re.findall(r"(\d+)", match.group("winning_numbers"))]
        your_numbers = [int(number) for number in re.findall(r"(\d+)", match.group("your_numbers"))]
        return cls(card_id, winning_numbers, your_numbers)

    def get_total_matches(self):
        total_matches = sum(1 for number in self.your_numbers if number in self.winning_numbers)
        return total_matches

    def get_points(self):
        total_matches = self.get_total_matches()
        if total_matches == 0:
            return 0
        points = 2 ** (total_matches - 1)
        return points


def part_1(cards):
    total = 0
    for card in cards:
        total += card.get_points()
    return total


def part_2(cards):
    card_totals = defaultdict(int)
    for card in cards:
        # Original
        card_totals[card.id] += 1
        # Create Copies
        for i in range(card.get_total_matches()):
            card_totals[card.id + i + 1] += card_totals[card.id]
    total = sum(card_totals.values())
    return total
