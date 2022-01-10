"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
"""
class RegularCard:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

queen_of_hearts = RegularCard('Q', 'Hearts')

print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == RegularCard('Q', 'Hearts'))