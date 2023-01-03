class Steel_armor():
    def __init__(self):
        self.__additional_dfnc = 6
        self.__armors_name = "Steel"

    def get_heavy_armor_deffence(self):
        return self.__additional_dfnc

    def get_armors_name(self):
        return self.__armors_name


class Ebony_armor():
    def __init__(self):
        self.__additional_dfnc = 9
        self.__armors_name = "Ebony"

    def get_heavy_armor_deffence(self):
        return self.__additional_dfnc

    def get_armors_name(self):
        return self.__armors_name