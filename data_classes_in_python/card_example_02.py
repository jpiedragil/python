"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#advanced-default-values
"""
from dataclasses import dataclass
from typing import List


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():

    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class PlayingCard:

    rank: str
    suit: str

@dataclass
class Deck:
    
    cards: List[PlayingCard]

print(make_french_deck())