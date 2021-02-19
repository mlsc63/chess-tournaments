from models.menu_model import MenuModel
from views.menu_view import MenuView
from list import ListObjet
from . import home_menu_controller
from views.data_table_view import DataTableView
# TODO Make better data management

class Init:

    def __init__(self, objet, value, tournament=''):
        self.objet = objet
        self.value = value
        self.tournament = tournament

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

        if self.value == 'round':
            table_match = []
            index = []
            columns = ['player 1', 'score', 'player 2', 'score']
            number_of_matches = 1

            for match in self.objet.get_match_list():
                table_match.append([self.tournament.get_players_instantiation_list()[match[0][0]].get_name_player(),
                                    match[0][1],
                                    self.tournament.get_players_instantiation_list()[match[1][0]].get_name_player(),
                                    match[1][1]])

                index.append(number_of_matches)
                number_of_matches += 1

            DataTableView(table_match, index, columns).display()

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

###########################################################################################
class ListOfAllMatchesInATournamentv2:
    def __init__(self, tournament):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        print('___Selectionner un tournois pour avoir la liste des tours___')
        for round in self.tournament.get_round_list():
            if round.get_status_round() == False:
                self.tournament_menu.add("auto", round.get_name_round(), Init(round, 'round', self.tournament))
            self.tournament_menu.add("r", 'Retour', home_menu_controller.HomeMenuController())


        user_choice = self.tournament_view.get_user_choice
        return user_choice



class ListOfAllMatchesInATournament:
    def __init__(self):
        self.tournament_menu = MenuModel()
        self.tournament_view = MenuView(self.tournament_menu)

    def __call__(self, *args, **kwargs):
        print('___Selectionner un tournois pour avoir la liste des tours___')
        for tournament in ListObjet.TOURNAMENT:

            self.tournament_menu.add("auto", tournament.get_name_tournament(),
                                     ListOfAllMatchesInATournamentv2(tournament))

        user_choice = self.tournament_view.get_user_choice
        return user_choice










