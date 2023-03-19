from skfuzzy import control as ctrl
from picasha import Picasha


class Fuzzirules():
    def __init__(self):
        picasha = Picasha()
        picasha.ling_var()
        self.humidity = picasha.humidity
        self.temperature = picasha.temperature
        self.distance_to_obstacle = picasha.distance_to_obstacle
        self.desired_speed = picasha.desired_speed
        self.rules = []
        self.set_rules()

    def set_rules(self):
        # Построение правил для нечеткой логики
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['cold'] & self.distance_to_obstacle['close'], self.desired_speed['slow']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['cold'] & self.distance_to_obstacle['medium'], self.desired_speed['slow']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['cold'] & self.distance_to_obstacle['far'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['medium'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['medium'] & self.distance_to_obstacle['medium'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['medium'] & self.distance_to_obstacle['far'], self.desired_speed['fast']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['hot'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['hot'] & self.distance_to_obstacle['medium'], self.desired_speed['fast']))
        self.rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['hot'] & self.distance_to_obstacle['far'], self.desired_speed['fast']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['cold'] & self.distance_to_obstacle['close'], self.desired_speed['slow']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['cold'] & self.distance_to_obstacle['medium'], self.desired_speed['slow']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['cold'] & self.distance_to_obstacle['far'], self.desired_speed['slow']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['medium'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['medium'] & self.distance_to_obstacle['medium'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['medium'] & self.distance_to_obstacle['far'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['hot'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['hot'] & self.distance_to_obstacle['medium'], self.desired_speed['fast']))
        self.rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['hot'] & self.distance_to_obstacle['far'], self.desired_speed['fast']))
