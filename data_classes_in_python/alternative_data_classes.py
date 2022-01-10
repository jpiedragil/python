"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#alternatives-to-data-classes
"""
queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}

print(queen_of_hearts_tuple[0])
print(queen_of_hearts_dict['suit'])

from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

queen_of_hearts = NamedTupleCard('Q', 'Hearts')

print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == NamedTupleCard('Q', 'Hearts'))

print(queen_of_hearts == ('Q', 'Hearts'))

Person = namedtuple('Person', ['first_initial', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')

print(ace_of_spades == Person('A', 'Spades'))

card = NamedTupleCard('7', 'Diamonds')
card.rank = '9'