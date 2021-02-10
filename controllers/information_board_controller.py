from models.menu_model import MenuModel
from views.menu_view import MenuView
from list import ListObjet
from . import home_menu_controller
from views.data_table_view import DataTableView


class Init:

    def __init__(self, objet, value):
        self.objet = objet
        self.value = value

    def __call__(self, *args, **kwargs):
        if self.value == "list_of_all_players_in_a_tournament":
            table_players = []
            index = []
            columns = ['Prenom', 'nom', 'Date de naissance', 'sexe', 'Classement']
            number_of_players = 1

            for player in self.objet.get_players_instantiation_list():
                table_players.append(player.player_table())
                index.append(number_of_players)
                number_of_players += 1

            DataTableView(table_players, index, columns).display()

            return home_menu_controller.HomeMenuController()


        if self.value =="ListOfAllRoundsInATournament":
            table_rounds = []
            index = []
            columns = ['Nom', 'Debut', 'Fin', 'status']
            number_of_rounds = 1
            for round in self.objet.get_round_list():
                table_rounds.append(round.round_table())
                index.append(number_of_rounds)
                number_of_rounds += 1

            DataTableView(table_rounds, index, columns).display()
            return home_menu_controller.HomeMenuController()




class ListOfAllPlayersInATournament:

    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self):
        print('___Selectionner un tournois pour avoir la liste des joueurs___')

        for tournament in ListObjet.TOURNAMENT:
            self.tournament_menu.add("auto", tournament.get_name_tournament(),
                                     Init(tournament, 'list_of_all_players_in_a_tournament'))

        user_choice = self.tournament_view.get_user_choice

        return user_choice


class ListOfAllPlayers:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        table_players = []
        index = []
        columns = ['Prenom', 'nom', 'Date de naissance', 'sexe', 'Classement']
        number_of_players = 1

        for tournament in ListObjet.TOURNAMENT:
            for player in tournament.get_players_instantiation_list():
                table_players.append(player.player_table())
                index.append(number_of_players)
                number_of_players += 1

        DataTableView(table_players, index, columns).display()
        return home_menu_controller.HomeMenuController()


class ListOfAllTournaments:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        table_tournaments = []
        index = []
        columns = ['Nom du tournois', 'Lieu', 'Date', 'Nombre de tours', 'Controle de temps', 'Nombre de joueurs',
                   'description', 'statut']
        number_of_tournament = 1

        for tournament in ListObjet.TOURNAMENT:
            table_tournaments.append(tournament.tournament_table())
            index.append(number_of_tournament)
            number_of_tournament += 1

        DataTableView(table_tournaments, index, columns).display()
        return home_menu_controller.HomeMenuController()


class ListOfAllRoundsInATournament:
    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self, *args, **kwargs):
        print('___Selectionner un tournois pour avoir la liste des tours___')
        for tournament in ListObjet.TOURNAMENT:
            self.tournament_menu.add("auto", tournament.get_name_tournament(),
                                     Init(tournament, 'ListOfAllRoundsInATournament'))

        user_choice = self.tournament_view.get_user_choice
        return user_choice


class ListOfAllMatchesInATournament:
    def __init__(self):
        pass








