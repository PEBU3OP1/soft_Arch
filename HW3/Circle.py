from Figure import Figure
from math import pi

class Circle(Figure):

    def __init__(self, radius: float):
        if radius > 0:
            self.__name = "Круг"
            self.__radius = radius
        else:
            print("Неверные параметры круга")


    def area(self) -> float:
        return (pi * pow(self.__radius, 2)).__round__(4)

    def perim(self)-> float:
        return (2 * pi * self.__radius).__round__(4)

    def __str__(self) -> str:
        return "Имя: " + self.__name + ", Радиус: " + str(self.__radius) + ", Площадь: " +\
               str(self.area()) + ", Длина окружности: " + str(self.perim())