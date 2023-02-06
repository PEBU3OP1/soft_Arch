import Circle
import Rectangle
import Triangle
from Figure import Figure
from Square import Square


class Program():
    def __init__(self):
        self.__area_perim_list = []


    def area_list(self, list_of_figures: list) -> list:
        for i in list_of_figures:
            self.__area_perim_list.append(i.area())
        return self.__area_perim_list

    def perim_list(self, list_of_figures: list) -> list:
        for i in list_of_figures:
            self.__area_perim_list.append(i.perim())
        return self.__area_perim_list

    def append_figure(self, list_of_figures_to_add: list, figure: Figure) -> list:
        list_of_figures_to_add.append(figure)
        return list_of_figures_to_add

    def info (self, list_of_figures: list) -> dict:
        final_dict = {}
        for i in range(len(list_of_figures)):
            final_dict[i] = str(list_of_figures[i])
        return final_dict

    def main(self):
        c = Circle.Circle(4)
        a = Square(3)
        b = Triangle.Triangle(3,3,4)
        e = Rectangle.Rectangle(3,2)

        d = [a, b, c, e]

        print(self.info(d))
        # print(Program().info(d))


if __name__ == '__main__':
    Program().main()