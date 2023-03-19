from fuzzifikator import Fuzzifikator
from generator import Generator


def calculate_desired_speed(fields: dict):
    fuzzifikator = Fuzzifikator(
        humidity=fields["humidity"],
        temperature=fields["temperature"],
        distance_to_obstacle=fields["distance_to_obstacle"]
    )
    desired_speed = fuzzifikator.calculate_desired_speed()
    return desired_speed


def get_sensors():
    data = Generator().get_updated_data()
    return data

