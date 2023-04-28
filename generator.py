from random import randint, uniform

import settings


class Generator:
    def __init__(self):
        self.distance_to_obstacle: int
        self.temperature: int
        self.humidity: int
        self.cars_count: int
        self.current_location: list
        self.update_data()
        super().__init__()

    def update_data(self):
        self.distance_to_obstacle = randint(*settings.DISTANCE_PEAKS)
        self.temperature = randint(*settings.TEMPERATURE_PEAKS)
        self.humidity = randint(*settings.HUMIDITY_PEAKS)
        self.cars_count = randint(*settings.CARS_COUNT_PEAKS)
        self.current_location = [uniform(*settings.LATITUDE_PEAKS), uniform(*settings.LONGITUDE_PEAKS)]

    def get_updated_data(self):
        self.update_data()
        data = {
            "distance_to_obstacle": self.distance_to_obstacle,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "cars_count": self.cars_count,
            "current_location": self.current_location,
        }
        return data
