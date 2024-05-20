from colorpoint import ColorPoint
#the idea is to makex and y protected from being written after initialization
class AdvancedColorPoint(ColorPoint):
    def __init__(self, x, y, color): #this is a magic method,
        self._x = x
        self._y = y
        self._color = color
 #all of these property functions are to ensure read only except for color
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color
    @color.setter #this allows you to put in values
    def color(self, color):
        self._color = color

new_point = AdvancedColorPoint(10, 10, "blue")
print(new_point)

print(new_point)