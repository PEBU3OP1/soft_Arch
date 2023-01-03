from Swords import Best_sword
from Swords import Normal_sword

import random

from Heavy_armor import Steel_armor, Ebony_armor

class Swordsman():
    def __sword_choosing(self):
        sword_choose = random.randint(0, 1)
        if sword_choose:
            sword = Best_sword()
        else:
            sword = Normal_sword()
        return sword


    def __heavy_armor_choosing(self):
        armor_choose = random.randint(0,1)
        if armor_choose:
            armor = Steel_armor()
        else:
            armor = Ebony_armor()
        return armor




    def __init__(self, side:str, enemy_side: list):
        self.__name = 'Swordsman'
        self.__health = 20
        self.__state = 'Alive'
        self.__sword = self.__sword_choosing()
        self.__heavy_armor = self.__heavy_armor_choosing()
        self.__attack = 6 + self.__sword.get_damage()
        self.__deffence = 7 + self.__heavy_armor.get_heavy_armor_deffence()
        self.__side = side
        self.__enemy_side = enemy_side
        self.__armors_name = self.__heavy_armor.get_armors_name()
        self.__swords_name = self.__sword.get_swords_name()

    def __str__(self):
        return self.__name + "; Hlth: " + str(self.__health) + "; Attck: " + str(self.__attack) + "; Dffnc " \
               + str(self.__deffence) + "; Sword: " + self.__swords_name + "; Heavy Armor: " \
               + self.__armors_name + "; hit: " + self.__enemy_side[0].get_name()



    def get_name(self):
        return self.__name

    def get_damage_from_enmemy (self):
        self.__health = self.__health - int(self.__enemy_side[0].get_attack()*(1 - float(self.__deffence /100)))

    def get_attack(self):
        return self.__attack

    def get_deffence(self):
        return self.__deffence

    def get_side(self):
        return self.__side

    def check_state(self):
        if self.__health <= 0:
            self.__state = "DEAD"
            self.__name = "X"
            return False
        return True