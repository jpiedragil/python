"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#more-flexible-data-classes
"""
from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:

    rank: str
    suit: str

@dataclass
class Deck:

    cards: List[PlayingCard]

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])

print(two_cards)