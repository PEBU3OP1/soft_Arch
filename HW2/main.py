from Archer import  Archer
import random
from Swordsman import Swordsman
from playing_field import one_field

class Program():
    def teams_adding(self, team: list, side: str, enemy_side: list) -> list:
        hero_choosing = random.randint(0,1)
        if hero_choosing:
            hero = Archer(side, enemy_side)

        else:
            hero = Swordsman(side, enemy_side)
        team.append(hero)
        return team

    def main(self):
            team1 = []
            team2 = []

            Program().teams_adding(team=team1, side='Red', enemy_side=team2)
            Program().teams_adding(team=team2, side='Blue', enemy_side=team1)



            while True:

                one_field(str(team1[0].get_name())[0], str(team2[0].get_name())[0], str(team1[0]), str(team2[0]))
                team2[0].get_damage_from_enmemy ()


                if not team1[0].check_state():
                    print("Blue wins!!")
                    one_field(str(team1[0].get_name())[0], str(team2[0].get_name())[0], str(team1[0]), str(team2[0]))

                    break
                if not team2[0].check_state():
                    print("Red wins!!")
                    one_field(str(team1[0].get_name())[0], str(team2[0].get_name())[0], str(team1[0]), str(team2[0]))

                    break
                team1[0].get_damage_from_enmemy()
                input("Жми Enter" )

if __name__ == '__main__':
    Program().main()

