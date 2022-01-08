"""
Source code from Dev.to article "Why you Should Use Python Data Classes" by
Omri Grossman.

URL: https://dev.to/omrigm/why-you-should-use-python-data-classes-48po
"""
class Car:

    color: str
    manufacturer: str
    top_speed_km: int

    def __init__(self,
                 color: str,
                 manufacturer: str,
                 top_speed_km: int):

        self.color = color
        self.manufacturer = manufacturer
        self.top_speed_km = top_speed_km

    def __lt__(self, other_car):

        return self.top_speed_km < other_car.top_speed_km

red_ferrari = Car(color='red',
                  manufacturer='Ferrari',
                  top_speed_km=320)

print(red_ferrari)

black_ferrari = Car(color='black',
                    manufacturer='Ferrari',
                    top_speed_km=347)

print(red_ferrari < black_ferrari)
