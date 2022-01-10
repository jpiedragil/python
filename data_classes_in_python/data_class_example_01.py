"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
"""
from dataclasses import dataclass


@dataclass
class DataClassCard:

    rank: str
    suit:str

queen_of_hearts = DataClassCard('Q', 'Hearts')

print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


