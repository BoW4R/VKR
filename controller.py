import settings
from fuzzifikator import DistanceFuzzifikator, TurnFuzzificator
from generator import Generator
from geopy import distance


def get_desired_speed(fields: dict):
    fuzzifikator = DistanceFuzzifikator(
        humidity=fields["humidity"],
        temperature=fields["temperature"],
        distance_to_obstacle=fields["distance_to_obstacle"]
    )
    desired_speed = fuzzifikator.calculate_desired_speed()
    return desired_speed


def get_turn_direction(fields: dict):
    fuzzifikator = TurnFuzzificator(
        speed=fields["desired_speed"],
        cars_count=fields["cars_count"],
        distance_to_obstacle=fields["distance_to_obstacle"]
    )
    turn_direction = fuzzifikator.calculate_turn_direction()
    return turn_direction


def get_closest_gas_station(current_location: list):
    list_of_distances = [distance.distance(current_location, station).km for station in settings.GAS_STATIONS_COORDS]
    return round(min(list_of_distances))

def get_sensors():
    data = Generator().get_updated_data()
    return data

