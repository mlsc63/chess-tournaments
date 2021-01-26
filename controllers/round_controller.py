from list import ListObjet
from . import home_menu_controller


class RoundController:

    def __init__(self):
        self.list_tournaments = ListObjet.TOURNAMENT

    def __call__(self):

        index = 0
        print('___Rounds en cour___')
        # get objet in the list on list.py
        for tournament in self.list_tournaments:
            print(tournament.get_name_tournament())

            print(tournament.get_round_list())
            # get objet on the tournament model and get information with round modelvd
            for round_in_tournament in tournament.get_round_list():
                print(round_in_tournament)

        input()
        return home_menu_controller.HomeMenuController()






