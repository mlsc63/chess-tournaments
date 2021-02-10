from models.menu_model import MenuModel
from views.menu_view import MenuView
from list import ListObjet
import numpy as np


class InitTable:

    def __init__(self, objet, value):
        self.objet = objet
        self.value = value

    def __call__(self, *args, **kwargs):
        if self.value == "list_of_all_players_in_a_tournament":
            table_players = []
            for player in self.objet.get_players_instantiation_list():
                table_players.append(player.player_table())
            table_players_numpy = np.array(table_players)
            print(table_players_numpy)



class ListOfAllPlayersInATournament:

    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self):
        print('___Selectionner un tournois pour avoir la liste des joueurs___')

        for tournament in ListObjet.TOURNAMENT:
            self.tournament_menu.add("auto", tournament.get_name_tournament(),
                                     InitTable(tournament, 'list_of_all_players_in_a_tournament'))

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
