from Figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        if side_a > 0 and side_b >0:
            self.__name = "Прямоугольник"
            self.__side_a = side_a
            self.__side_b = side_b
        else:
            print("Неверные параметры прямоугольника")


    def perim(self) -> float:
        return 2*self.__side_a + 2*self.__side_b

    def area(self)-> float:
        return self.__side_a * self.__side_b

    def __str__(self) -> str:
        return "Имя: " + self.__name + ", длина стороны A: " + str(self.__side_a) + ", Длина стороны B: " +\
               str(self.__side_b) + ", Площадь: " + str(self.area()) + ", Периметр: " + str(self.perim())

