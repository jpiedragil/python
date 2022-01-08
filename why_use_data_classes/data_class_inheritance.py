"""
Source code from Dev.to article "Why you Should Use Python Data Classes" by
Omri Grossman.

URL: https://dev.to/omrigm/why-you-should-use-python-data-classes-48po
"""
from dataclasses import dataclass

@dataclass
class Car:

    color: str
    manufacturer: str
    top_speed_km: int

@dataclass
class ElectricCar(Car):

    battery_capacity_kwh: int
    maximum_range_km: int

white_tesla_model_3 = ElectricCar(color='white',
                                  manufacturer='Tesla',
                                  top_speed_km=261,
                                  battery_capacity_kwh=50,
                                  maximum_range_km=455)

print(white_tesla_model_3)
