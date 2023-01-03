class Best_bow():
    def __init__(self):
        self.__name = "Best bow"
        self.__additional_dmg = 6

    def get_damage(self):
        return self.__additional_dmg

    def get_bow_name(self):
        return self.__name


class Normal_bow():
    def __init__(self):
        self.__name = "Normal bow"
        self.__additional_dmg = 3

    def get_damage(self):
        return self.__additional_dmg

    def get_bow_name(self):
        return self.__name