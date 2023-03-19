from random import randint


class Generator():
    def __init__(self):
        self.distance_to_obstacle: int
        self.temperature: int
        self.humidity: int
        self.update_data()
        super().__init__()

    def update_data(self):
        self.distance_to_obstacle = randint(0, 200)
        self.temperature = randint(-40, 40)
        self.humidity = randint(0, 100)

    def get_updated_data(self):
        self.update_data()
        data = {
            "distance_to_obstacle": self.distance_to_obstacle,
            "temperature": self.temperature,
            "humidity": self.humidity,
        }
        return data
