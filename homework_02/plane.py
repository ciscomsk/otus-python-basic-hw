"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 1000

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, weight: int):
        loaded_cargo = self.cargo + weight
        if loaded_cargo < self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload(f'Overload: current cargo + weight - {loaded_cargo}, max cargo - {self.max_cargo}')

    def remove_all_cargo(self):
        unloaded_cargo = self.cargo
        self.cargo = 0
        return unloaded_cargo
