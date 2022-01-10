"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
"""
class RegularCard:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

    def __repr__(self):

        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):

        if other.__class__ is not self.__class__:

            return NotImplemented

        return (self.rank, self.suit) == (other.rank, other.suit)

queen_of_hearts = RegularCard('Q', 'Hearts')

print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == RegularCard('Q', 'Hearts'))