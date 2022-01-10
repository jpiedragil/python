"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#advanced-default-values
"""
from dataclasses import dataclass, field, fields
from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:

    name: str
    lon: float = field(default=0.0,metadata={'unit': 'degrees'})
    lat: float = field(default=0.0,metadata={'unit': 'degrees'})

    def distance_to(self, other):

        r = 6371 # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)

        return 2 * r * asin(sqrt(h))

print(fields(Position))

lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)