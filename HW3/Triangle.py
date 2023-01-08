from Figure import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, side_a: float, side_b:float, side_c:float):
        if side_a + side_b <= side_c or side_b + side_c <= side_a\
            or side_a + side_c <= side_b:
            print("Неверные параметры")
        else:
            self.__name = "Треугольник"
            self.__side_a = side_a
            self.__side_b = side_b
            self.__side_c = side_c

    def area(self)-> float:
        p = (self.__side_a + self.__side_b + self.__side_c)/2
        s = sqrt(p*(p - self.__side_a)* (p-self.__side_b) * (p-self.__side_c))
        return s.__round__(4)

    def perim(self)-> float:
        p = self.__side_a + self.__side_b + self.__side_c
        return p.__round__(4)

    def __str__(self) -> str:
        return "Имя: " + self.__name + ", длина стороны A: " + str(self.__side_a) + ", Длина стороны B: " +\
               str(self.__side_b) + ", длина стороны С: " + str(self.__side_c) + ", Площадь: " + str(self.area()) + \
               ", Периметр: " + str(self.perim())
