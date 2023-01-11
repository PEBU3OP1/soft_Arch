from Bows import Best_bow, Normal_bow

import random

from Light_armor import Leather_armor, Glass_armor


class Archer():
    """методы для рандомного выбора лука и легкой брони при создании класса Archer """

    def __bow_choosing(self):
        bow_choose = random.randint(0, 1)
        if bow_choose:
            bow = Best_bow()
        else:
            bow = Normal_bow()
        return bow

    def __light_armor_choosing(self):
        armor_choose = random.randint(0, 1)
        if armor_choose:
            armor = Leather_armor()
        else:
            armor = Glass_armor()
        return armor

    """ здесь к защите/атаке прирастает значения от полученного лука/брони
    также использую имя лука/брони, определяю противную сторону. На самом деле нужно было делать родительский
        базовый класс и там реализовывать основные методы / переменные"""
    def __init__(self, side: str, enemy_side: list):
        self.__name = 'Archer'
        self.__health = 15
        self.__state = 'Alive'
        self.__bow = self.__bow_choosing()
        self.__light_armor = self.__light_armor_choosing()
        self.__attack = 8 + self.__bow.get_damage()
        self.__deffence = 4 + self.__light_armor.get_armor_dfnc()
        self.__side = side
        self.__enemy_side = enemy_side
        self.__light_armors_name = self.__light_armor.get_light_armor_name()
        self.__bows_name = self.__bow.get_bow_name()
    """это использую для вывода инф на экран"""
    def __str__(self):
        return self.__name + "; Hlth: " + str(self.__health) + "; Attck: " + str(self.__attack) + "; Dffnc " \
              + str(self.__deffence) +"; Bow: "+ self.__bows_name + "; Light Armor: "\
               + self.__light_armors_name+"; hit: " + self.__enemy_side[0].get_name()



    def get_damage_from_enmemy (self):
        self.__health = self.__health - int(self.__enemy_side[0].get_attack()*(1 - float(self.__deffence /100)))
    def check_state(self):
        if self.__health <= 0:
            self.__state = "DEAD"
            self.__name = "X"
            return False
        return True

    """данные методы использовал в процессе создания, в данном примере носят информативный характер"""
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health

    def get_attack(self):
        return self.__attack

    def get_deffence(self):
        return self.__deffence

    def get_side(self):
        return self.__side

