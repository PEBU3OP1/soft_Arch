class Leather_armor():
    def __init__(self):
        self.__additional_dfnc = 4
        self.__armor_name = "Leather"

    def get_armor_dfnc(self):
        return self.__additional_dfnc

    def get_light_armor_name(self):
        return self.__armor_name


class Glass_armor():
    def __init__(self):
        self.__additional_dfnc = 8
        self.__armor_name = "Glass"

    def get_armor_dfnc(self):
        return self.__additional_dfnc

    def get_light_armor_name(self):
        return self.__armor_name