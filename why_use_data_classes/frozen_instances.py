"""
Source code from Dev.to article "Why you Should Use Python Data Classes" by
Omri Grossman.

URL: https://dev.to/omrigm/why-you-should-use-python-data-classes-48po
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Car:

    color: str
    manufacturer: str
    top_speed_km: int

white_tesla = Car(color='white',
                  manufacturer='Tesla',
                  top_speed_km=261)
white_tesla.color = 'Red'


