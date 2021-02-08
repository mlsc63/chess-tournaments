from tinydb import TinyDB, Query
from list import ListObjet
from . import home_menu_controller
from models.tournament_model import TournamentsModel


class DataControllerSave:
    def __init__(self):
        self.db = TinyDB("db_tournaments.json")
        self.db_table_tournaments = self.db.table('tournaments')
        self.db_table_players = self.db.table('players')
        self.db_table_rounds = self.db.table('rounds')

    def __call__(self):

        # we erase all table from db
        DataControllerErase()
        # we search all tournament
        index = 1
        for tournament in ListObjet.TOURNAMENT:
            self.db_table_tournaments.insert(tournament.get_instantiation_serialisation_tournament())
            # In each tournament we search all players
            for player in tournament.get_players_instantiation_list():
                self.db_table_players.insert(player.get_instantiation_serialisation_player(index))
            # In each tournament we search all rounds
            for round in tournament.get_round_list():
                self.db_table_rounds.insert(round.get_instantiation_serialisation_round(index))

            index += 1
            return home_menu_controller.HomeMenuController()


class DataControllerErase:
    def __init__(self):
        self.db = TinyDB("db_tournaments.json")
        self.db_table_tournaments = self.db.table('tournaments')
        self.db_table_players = self.db.table('players')
        self.db_table_rounds = self.db.table('rounds')

    def __call__(self):
        self.db_table_tournaments.truncate()
        self.db_table_players.truncate()
        self.db_table_rounds.truncate()
        return home_menu_controller.HomeMenuController()


class DataControllerLoad:
    def __init__(self):
        self.db = TinyDB("db_tournaments.json")
        self.db_table_tournaments = self.db.table('tournaments')
        self.db_table_players = self.db.table('players')
        self.db_table_rounds = self.db.table('rounds')

    def __call__(self):
        for tournament in self.db_table_tournaments:
            # print(tournament)
            self.tournament_model = TournamentsModel(tournament['name'])
            ListObjet.TOURNAMENT.append(self.tournament_model)
            print(tournament['name'])

    # db_tournaments.insert({'name': 'jhone', 'age': '10'})
    # print(db_tournaments.all())
