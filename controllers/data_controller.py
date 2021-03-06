from tinydb import TinyDB, Query
from list import ListObjet
from . import home_menu_controller
from models.tournament_model import TournamentsModel
from models.player_model import PlayerModel
from models.round_model import RoundModel


class DataControllerSave:
    """
    Before saving, we delete all the data in the JSON files.
     The tournaments to be saved are in the list (ListObjet).
    Work with three tables (Tournaments, players, and rounds)
    Serialization is done directly by object methods,
     only an index and given as a parameter to index certain data
    """

    def __init__(self):
        self.db = TinyDB("db_tournaments.json")
        self.db_table_tournaments = self.db.table('tournaments')
        self.db_table_players = self.db.table('players')
        self.db_table_rounds = self.db.table('rounds')

    def __call__(self):

        # we erase all table from db
        data_controller_erase = DataControllerErase()
        data_controller_erase()
        # we search all tournament
        index = 1
        for tournament in ListObjet.TOURNAMENT:

            self.db_table_tournaments.insert(
                tournament.get_instantiation_serialisation_tournament())
            # In each tournament we search all players
            for player in tournament.get_players_instantiation_list():
                self.db_table_players.insert(
                    player.get_instantiation_serialisation_player(index))
            # In each tournament we search all rounds
            for round in tournament.get_round_list():
                self.db_table_rounds.insert(
                    round.get_instantiation_serialisation_round(index))

            index += 1
        return home_menu_controller.HomeMenuController()


class DataControllerErase:
    """
    Clear all three tables
    """

    def __init__(self):
        self.db = TinyDB("db_tournaments.json")
        self.db_table_tournaments = self.db.table('tournaments')
        self.db_table_players = self.db.table('players')
        self.db_table_rounds = self.db.table('rounds')

    def __call__(self):
        self.db_table_tournaments.truncate()
        self.db_table_players.truncate()
        self.db_table_rounds.truncate()


class DataControllerLoad:
    """
    Try to read the data. Otherwise we consider that there is no data.
    We load the tournaments,
    then the players who have an equal idea of the tournaments,
    then we do the same with the rounds
    """

    def __init__(self):
        self.db = TinyDB("db_tournaments.json")
        self.db_table_tournaments = self.db.table('tournaments')
        self.db_table_players = self.db.table('players')
        self.db_table_rounds = self.db.table('rounds')
        self.tournament_model = ''
        self.player_model = ''
        self.round_model = ''
        self.query = Query()

    def __call__(self):
        try:
            index = 1

            for tournament in self.db_table_tournaments:
                self.tournament_model = TournamentsModel(
                    tournament['name'],
                    tournament['location'],
                    tournament['date'],
                    tournament['number_of_turns'],
                    tournament['time_controller'],
                    tournament['number_of_players'],
                    tournament['description'],
                    tournament['status'],
                    tournament['score'],
                    tournament['meet'])

                ListObjet.TOURNAMENT.append(self.tournament_model)
                for player in self.db_table_players.search(
                        self.query.index == index):
                    self.player_model = PlayerModel(player['first_name'],
                                                    player['name'],
                                                    player['date_of_bird'],
                                                    player['sex'],
                                                    player['ranked'],
                                                    self.tournament_model,
                                                    player['id']
                                                    )
                    # We add instantiation player in tournament model
                    self.tournament_model.add_instantiation_players(
                        self.player_model)

                for round in self.db_table_rounds.search(
                        self.query.index == index):
                    self.round_model = RoundModel(round['name'],
                                                  self.tournament_model,
                                                  round['start_time'],
                                                  round['end_time'],
                                                  round['match_list'],
                                                  round['status'],
                                                  )

                    # We add instantiation round in tournament model
                    self.tournament_model.add_round_list_tournament(
                        self.round_model)

                index += 1

        except ValueError:
            print('___No DATA___')
