class Best_sword():
    def __init__(self):
        self.__additional_dmg = 3
        self.__sword_name = "Best Sword"

    def get_damage(self):
        return self.__additional_dmg


    def get_swords_name(self):
        return self.__sword_name

class Normal_sword():
    def __init__(self):
        self.__additional_dmg = 1
        self.__sword_name = "Normal Sword"

    def get_damage(self):
        return self.__additional_dmg

    def get_swords_name(self):
        return self.__sword_name