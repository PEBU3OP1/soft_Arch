
class Model ():
    def __init__(self, id: int, location: str, angle: int):
        self.__id = id
        self.__location = location
        self.__angle = angle

    def __str__(self):
        return 'ID: ' + str(self.__id) + '\n' \
               + 'Location: ' + self.__location + '\n' \
               + 'Angle: ' + str(self.__angle)

    def move(self):
        pass

    def rotate(self):
        pass