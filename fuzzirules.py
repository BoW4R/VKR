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
        self.speed = picasha.speed
        self.cars_count = picasha.cars_count
        self.turn_direction = picasha.turn_direction

    def get_turn_direction_rules(self):
        turn_direction_rules = []
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["close"] & self.cars_count["cars_none"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["close"] & self.cars_count["cars_some"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["close"] & self.cars_count["cars_many"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_none"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_some"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_many"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["far"] & self.cars_count["cars_none"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["far"] & self.cars_count["cars_some"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["slow"] & self.distance_to_obstacle["far"] & self.cars_count["cars_many"], self.turn_direction["direction_right"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["close"] & self.cars_count["cars_none"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["close"] & self.cars_count["cars_some"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["close"] & self.cars_count["cars_many"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_none"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_some"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_many"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["far"] & self.cars_count["cars_none"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["far"] & self.cars_count["cars_some"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["medium"] & self.distance_to_obstacle["far"] & self.cars_count["cars_many"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["close"] & self.cars_count["cars_none"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["close"] & self.cars_count["cars_some"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["close"] & self.cars_count["cars_many"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_none"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_some"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["medium"] & self.cars_count["cars_many"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["far"] & self.cars_count["cars_none"], self.turn_direction["direction_straight"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["far"] & self.cars_count["cars_some"], self.turn_direction["direction_left"]))
        turn_direction_rules.append(ctrl.Rule(self.speed["fast"] & self.distance_to_obstacle["far"] & self.cars_count["cars_many"], self.turn_direction["direction_left"]))
        return turn_direction_rules
    
    def get_desired_speed_rules(self):
        # Построение правил для нечеткой логики
        desired_speed_rules = []
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['cold'] & self.distance_to_obstacle['close'], self.desired_speed['slow']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['cold'] & self.distance_to_obstacle['medium'], self.desired_speed['slow']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['cold'] & self.distance_to_obstacle['far'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['medium'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['medium'] & self.distance_to_obstacle['medium'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['medium'] & self.distance_to_obstacle['far'], self.desired_speed['fast']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['hot'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['hot'] & self.distance_to_obstacle['medium'], self.desired_speed['fast']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['low'] & self.temperature['hot'] & self.distance_to_obstacle['far'], self.desired_speed['fast']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['cold'] & self.distance_to_obstacle['close'], self.desired_speed['slow']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['cold'] & self.distance_to_obstacle['medium'], self.desired_speed['slow']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['cold'] & self.distance_to_obstacle['far'], self.desired_speed['slow']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['medium'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['medium'] & self.distance_to_obstacle['medium'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['medium'] & self.distance_to_obstacle['far'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['hot'] & self.distance_to_obstacle['close'], self.desired_speed['medium']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['hot'] & self.distance_to_obstacle['medium'], self.desired_speed['fast']))
        desired_speed_rules.append(ctrl.Rule(self.humidity['high'] & self.temperature['hot'] & self.distance_to_obstacle['far'], self.desired_speed['fast']))
        return desired_speed_rules
