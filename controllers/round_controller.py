from list import ListObjet
from . import home_menu_controller


class RoundController:

    def __init__(self):
        self.list_tournaments = ListObjet.TOURNAMENT

    def __call__(self):

        index = 0
        for tournament in self.list_tournaments:
            print(tournament.get_name_tournament())

            print(tournament.get_round_list())
            for j in tournament.get_round_list():
                print(j)

        input()
        return home_menu_controller.HomeMenuController()






