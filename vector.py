from __future__ import annotations
import math
import random

class Vector:
    def __init__(self, x: int | float,
                 y: int | float,
                 z: int | float,
                 ):
        self.__check_elem(x)
        self.__x = x

        self.__check_elem(y)
        self.__y = y

        self.__check_elem(z)
        self.__z = z

    def __str__(self):
        return (f"x: {self.__x},"
                f"y: {self.__y,}"
                f"z: {self.__z}")
    
    def __check_elem(self, elem):
        if not isinstance(elem, (int, float)):
            raise TypeError("ne tot tip")
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z
    
    def length(self):
        return round((self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5, 2)
    
    def add(self, other: Vector):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
    
    def sub(self, other: Vector):
        return Vector(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
    
    def scalar_mul(self, other: Vector):
        return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z
    
    def angle_between(self, other: Vector):
        if self.length() == 0 or other.length() == 0:
            raise ZeroDivisionError('аларм аларм аларм')
        
        cos = round(self.scalar_mul(other) / (self.length() * other.length()), 2)
        if cos > 1 or cos < -1:
            raise ValueError(f'{cos}')
        
        return round(math.acos(cos), 2)
    
    def random(self):
        return Vector(random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100))