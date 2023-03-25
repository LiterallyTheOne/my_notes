from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def get_angles(self):
        pass


class Triangle(Polygon):
    def get_angles(self):
        return 3


class Rectangle(Polygon):
    def get_angles(self):
        return 4
