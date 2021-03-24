from list import ListObjet
from models.menu_model import MenuModel
from views.menu_view import MenuView
from .round_global_controller import RoundGlobalController
from . import home_menu_controller


class RoundMenuController:
    """
    Same principle as the HomeMenuController class:
     -We only display the first tournament that has not been done
    """

    def __init__(self):
        self.list_tournaments = ListObjet.TOURNAMENT
        self.round_menu = MenuModel()
        self.round_view = MenuView(self.round_menu)

    def __call__(self):

        print('___Rounds en cour___')

        # get objet in the list on list.py
        for tournament in self.list_tournaments:

            # If the tournament is done we don't display
            if tournament.get_status_tournament():

                # get objet on the tournament model,
                # and get information with round model
                for round_in_tournament in tournament.get_round_list():

                    if round_in_tournament.get_status_round():
                        # print(round_in_tournament)
                        self.round_menu.add(
                            "auto", 'Faire le '
                                    + round_in_tournament.get_name_round() +
                                    ' du tournoi: '
                                    + tournament.get_name_tournament() +
                                    '?',
                            RoundGlobalController(round_in_tournament))

                        # break -> we display only one
                        break
            self.round_menu.add("r",
                                'Retour',
                                home_menu_controller.HomeMenuController())

        users_choice = self.round_view.get_user_choice
        return users_choice
