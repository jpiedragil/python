"""
Source code from Dev.to article "Why you Should Use Python Data Classes" by
Omri Grossman.

URL: https://dev.to/omrigm/why-you-should-use-python-data-classes-48po
"""
from dataclasses import dataclass


@dataclass(order=True)
class Car:

    color: str
    manufacturer: str
    top_speed_km: int

slow_tesla = Car(top_speed_km=261, color='white', manufacturer='Tesla')
print(slow_tesla)

fast_tesla = Car(top_speed_km=280, color='white', manufacturer='Tesla')
print(slow_tesla < fast_tesla)
