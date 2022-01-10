"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#default-values
"""
from dataclasses import dataclass


@dataclass
class Position:

    name: str
    lon: float = 0.0
    lat: float = 0.0

print(Position('Null Island'))
print(Position('Greenwich', lat=51.8))
print(Position('Vancouver', -123.1, 49.3))
