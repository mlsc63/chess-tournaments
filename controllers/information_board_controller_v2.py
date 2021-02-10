from models.menu_model import MenuModel
from views.menu_view import MenuView
from list import ListObjet
from . import home_menu_controller
from views.data_table_view import DataTableView


class TournamentSelection:
    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self, *args, **kwargs):
        print('___Selectionner un tournois pour avoir la liste des joueurs___')

        for tournament in ListObjet.TOURNAMENT:
            self.tournament_menu.add("auto", tournament.get_name_tournament(), tournament.get_name_tournament())

        user_choice = self.tournament_view.get_user_choice
        return user_choice



class SelectRound:
    pass


class InitDisplay:
     pass

##############################################

class ListOfAllPlayersInATournament:
    def __init__(self):
        self.a = TournamentSelection()

    def __call__(self, *args, **kwargs):

        print(self.a)

class ListOfAllPlayers:
    pass


class ListOfAllTournaments:
    pass


class ListOfAllRoundsInATournament:
    pass


class ListOfAllMatchesInATournament:
    pass
