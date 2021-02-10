from models.menu_model import MenuModel
from views.menu_view import MenuView
from list import ListObjet


class ListOfAllPlayersInATournament:

    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self):
        print('___Selectionner un tournois pour avoir la liste des joueurs___')

        for tournament in ListObjet.TOURNAMENT:
            self.tournament_menu.add("auto", tournament.get_name_tournament(), lambda: None)

        user_choice = self.tournament_view.get_user_choice

        return user_choice


class ListOfAllPlayers:
    pass


class ListOfAllTournaments:
    pass


class ListOfAllRoundsInATournament:
    pass


class ListOfAllMatchesInATournament:
    pass
