"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#alternatives-to-data-classes
"""
import attr


@attr.s
class AttrsCard:

    rank = attr.ib()
    suit = attr.ib()

queen_of_hearts = AttrsCard('Q', 'Hearts')

print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == AttrsCard('Q', 'Hearts'))