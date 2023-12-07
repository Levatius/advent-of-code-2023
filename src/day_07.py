from collections import Counter
from dataclasses import dataclass
from enum import Enum

SPECIAL_CARD_STRENGTHS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "j": 1}


class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@dataclass
class Hand:
    cards: list[str]
    bid: int

    @classmethod
    def from_line(cls, line, part):
        cards, bid = line.split(" ")
        # We replace "J" with "j" to represent the jokers in part 2
        if part == 2:
            cards = cards.replace("J", "j")
        return cls(cards=list(cards), bid=int(bid))

    @staticmethod
    def _get_hand_type(ordered_counts, joker_count):
        match ordered_counts[0] + joker_count:
            case 5:
                return HandType.FIVE_OF_A_KIND
            case 4:
                return HandType.FOUR_OF_A_KIND
            case 3:
                match ordered_counts[1]:
                    case 2:
                        return HandType.FULL_HOUSE
                    case 1:
                        return HandType.THREE_OF_A_KIND
            case 2:
                match ordered_counts[1]:
                    case 2:
                        return HandType.TWO_PAIR
                    case 1:
                        return HandType.ONE_PAIR
            case 1:
                return HandType.HIGH_CARD

    @staticmethod
    def _get_card_strength(card):
        if card in SPECIAL_CARD_STRENGTHS:
            return SPECIAL_CARD_STRENGTHS[card]
        return int(card)

    def get_strength(self):
        counts = Counter(self.cards)
        joker_count = counts.pop("j") if ("j" in counts and counts.get("j") != 5) else 0
        ordered_counts = [count for _, count in counts.most_common()]

        hand_type = self._get_hand_type(ordered_counts, joker_count)

        # Concatenate into a large number that guarantees the hands can be ranked correctly:
        hand_type_strength = str(hand_type.value)
        card_strengths = "".join(f"{self._get_card_strength(card):02}" for card in self.cards)
        return int(hand_type_strength + card_strengths)


def part_x(hands):
    sorted_hands = sorted(hands, key=Hand.get_strength)
    return sum((i + 1) * hand.bid for i, hand in enumerate(sorted_hands))
