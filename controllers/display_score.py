from list import ListObjet
from views.menu_view import MenuView
from models.menu_model import MenuModel
from . import home_menu_controller
from views.data_table_view import DataTableView


class Init:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        columns = ['Prenom', 'Nom', 'score']
        table_players = []
        index = []
        number_of_players = 1
        index_player = 0

        for score in self.tournament.get_score():
            player = self.tournament.get_players_instantiation_list()[index_player]

            table_players.append([player.get_first_name_p(), player.get_name_p(), score])
            index.append(number_of_players)
            number_of_players += 1
            index_player += 1

        DataTableView(table_players, index, columns).display()
        return home_menu_controller.HomeMenuController()


class TournamentsScore:
    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self, *args, **kwargs):
        for tournament in ListObjet.TOURNAMENT:
            if not tournament.get_status_tournament():
                self.tournament_menu.add("auto", tournament.get_name_tournament(), Init(tournament))
            self.tournament_menu.add("r", 'Retour', home_menu_controller.HomeMenuController())

        user_choice = self.tournament_view.get_user_choice
        return user_choice
