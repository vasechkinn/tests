class Circle:
    def __init__(self, r: int | float):
        self.__check_elem(r)
        self.__r = r

    def __check_elem(self, r):
        if not isinstance(r, (int, float)):
            raise TypeError
        if r <= 0:
            raise ValueError('net')

    def __str__(self):
        return f"rad: {self.__r}"
    
    def get_r(self):
        return self.__r
    
    def area(self):
        return 3.14 * self.__r**2
    
    def circumference(self):
        return 2 * 3.14 *self.__r
    
    def diameter(self):
        return self.__r * 2
    
c = Circle(0.1)
print(c.area())
print(c.circumference())
print(c.diameter())