from abc import ABC

import exceptions


class Vehicle(ABC):
    weight = 1000
    started = False
    fuel = 100
    fuel_consumption = 5

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('No fuel')

    def move(self, distance):
        required_fuel = self.fuel_consumption * distance
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
        else:
            raise exceptions.NotEnoughFuel(f'Not enough fuel: available - {self.fuel}, required - {required_fuel}"')
