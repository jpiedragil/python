"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#you-need-representation
"""
from dataclasses import dataclass, field
from typing import List


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():

    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class PlayingCard:

    rank: str
    suit: str

    def __str__(self):

        return f'{self.suit}{self.rank}'

@dataclass
class Deck:
    
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):

        cards = ', '.join(f'{c!s}' for c in self.cards)

        return f'{self.__class__.__name__}({cards})'

ace_of_spades = PlayingCard('A', '♠')

print(ace_of_spades)
print(Deck())