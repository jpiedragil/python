"""
Source code from Dev.to article "Why you Should Use Python Data Classes" by
Omri Grossman.

URL: https://dev.to/omrigm/why-you-should-use-python-data-classes-48po
"""
class Car:

    color:str
    manufacturer: str
    top_speed_km: int

    def __init__(self,
                 color: str,
                 manufacturer: str,
                 top_speed_km: int):

        self.color = color
        self.manufacturer = manufacturer
        self.top_speed_km = top_speed_km

class ElectricCar(Car):

    battery_capacity_kwh: int
    maximum_range_km: int

    def __init__(self,
                 color: str,
                 manufacturer: str,
                 top_speed_km: int,
                 battery_capacity_kwh: int,
                 maximum_range_km: int):

        super().__init__(color, manufacturer, top_speed_km)
        self.battery_capacity_kwh = battery_capacity_kwh
        self.maximum_range_km = maximum_range_km

white_tesla_model_3 = ElectricCar(color='white',
                                  manufacturer='Tesla',
                                  top_speed_km=261,
                                  battery_capacity_kwh=50,
                                  maximum_range_km=455)
print(white_tesla_model_3)
