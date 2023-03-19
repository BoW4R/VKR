from fuzzirules import Fuzzirules
from skfuzzy import control as ctrl


class Fuzzifikator():
    def __init__(self, humidity, temperature, distance_to_obstacle):
        self.fuzzirules = Fuzzirules()
        self.humidity: int = humidity
        self.temperature: int = temperature
        self.distance_to_obstacle: int = distance_to_obstacle

    def calculate_desired_speed(self):
        # Define the control system and simulation
        control_system = ctrl.ControlSystem(self.fuzzirules.rules)
        simulation = ctrl.ControlSystemSimulation(control_system)
        simulation.input['humidity'] = self.humidity
        simulation.input['temperature'] = self.temperature
        simulation.input['distance_to_obstacle'] = self.distance_to_obstacle
        simulation.compute()
        return simulation.output['desired_speed']
