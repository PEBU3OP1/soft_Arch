from Figure import Figure

class Square (Figure):
    def __init__(self, side: float):
        if side > 0:
            self.__name = "Квадрат"
            self.__side = side
        else:
            print("Неверные параметры квадрата")


    def area(self) -> float:
        return self.__side * self.__side
    def perim(self) -> float:
        return self.__side*4

    def __str__(self) -> str:
        return "Имя: " + self.__name + ", длина стороны: " + str(self.__side) + ", Площадь: " +\
               str(self.area()) + ", Периметр: " + str(self.perim())