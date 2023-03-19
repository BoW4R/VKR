#from Model import *
#from Editor import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class Picasha():
    def __init__(self):
        # Определение входных переменных
        self.humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
        self.temperature = ctrl.Antecedent(np.arange(-40, 40, 1), 'temperature')
        self.distance_to_obstacle = ctrl.Antecedent(np.arange(0, 201, 1), 'distance_to_obstacle')
        # Определение выходной переменной
        self.desired_speed = ctrl.Consequent(np.arange(0, 101, 1), 'desired_speed')
        self.ling_var()

    def ling_var(self):
        # Определение функций принадлежности для каждой переменной

        self.humidity['low'] = fuzz.trimf(self.humidity.universe, [0, 0, 50])
        self.humidity['high'] = fuzz.trimf(self.humidity.universe, [50, 100, 100])

        self.temperature['cold'] = fuzz.trimf(self.temperature.universe, [-40, -40, 20])
        self.temperature['medium'] = fuzz.trimf(self.temperature.universe, [-40, 20, 40])
        self.temperature['hot'] = fuzz.trimf(self.temperature.universe, [20, 40, 40])

        self.distance_to_obstacle['close'] = fuzz.trimf(self.distance_to_obstacle.universe, [0, 0, 100])
        self.distance_to_obstacle['medium'] = fuzz.trimf(self.distance_to_obstacle.universe, [0, 100, 200])
        self.distance_to_obstacle['far'] = fuzz.trimf(self.distance_to_obstacle.universe, [100, 200, 200])

        self.desired_speed['slow'] = fuzz.trimf(self.desired_speed.universe, [0, 0, 50])
        self.desired_speed['medium'] = fuzz.trimf(self.desired_speed.universe, [0, 50, 100])
        self.desired_speed['fast'] = fuzz.trimf(self.desired_speed.universe, [50, 100, 100])

