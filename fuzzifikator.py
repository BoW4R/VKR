from fuzzirules import Fuzzirules
from skfuzzy import control as ctrl
from skfuzzy import defuzz
import numpy as np

class DistanceFuzzifikator:
    def __init__(self, humidity, temperature, distance_to_obstacle):
        self.fuzzirules = Fuzzirules()
        self.humidity: int = humidity
        self.temperature: int = temperature
        self.distance_to_obstacle: int = distance_to_obstacle

    def calculate_desired_speed(self):
        # Define the control system and simulation
        control_system = ctrl.ControlSystem(self.fuzzirules.get_desired_speed_rules())
        simulation = ctrl.ControlSystemSimulation(control_system)
        simulation.input['humidity'] = self.humidity
        simulation.input['temperature'] = self.temperature
        simulation.input['distance_to_obstacle'] = self.distance_to_obstacle
        simulation.compute()
        return simulation.output['desired_speed']


class TurnFuzzificator:
    def __init__(self, speed, cars_count, distance_to_obstacle):
        self.fuzzirules = Fuzzirules()
        self.speed: int = speed
        self.cars_count: int = cars_count
        self.distance_to_obstacle: int = distance_to_obstacle

    def calculate_turn_direction(self):
        # Define the control system and simulation
        control_system = ctrl.ControlSystem(self.fuzzirules.get_turn_direction_rules())
        simulation = ctrl.ControlSystemSimulation(control_system)
        simulation.input['speed'] = self.speed
        simulation.input['cars_count'] = self.cars_count
        simulation.input['distance_to_obstacle'] = self.distance_to_obstacle
        simulation.compute()

        # -0.67..-0.2 - объезжать слева
        # -0.2..0.2 - ехать прямо
        # 0.2..0.67 - объезжать справа
        if simulation.output['turn_direction'] <= -0.2:
            return "Левее "
        elif simulation.output['turn_direction'] >= 0.2:
            return "Правее"
        else:
            return "Прямо "
