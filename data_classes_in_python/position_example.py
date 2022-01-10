"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#basic-data-classes
"""
from dataclasses import dataclass


@dataclass
class Position:

    name: str
    lon: float
    lat: float

pos = Position('Oslo', 10.8, 59.9)
print(pos)

print(pos.lat)

print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')