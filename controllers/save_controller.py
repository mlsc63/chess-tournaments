from tinydb import TinyDB, Query
from list import ListObjet


class SaveController:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        db = TinyDB("db_tournaments.json")
        db_table_tournaments = db.table('tournaments')
        db_table_players = db.table('players')
        db_table_rounds = db.table('rounds')
        # db_table_tournaments.truncate() pour supprimer la table
        search = Query()

        # we search all tournament
        index = 1
        for tournament in ListObjet.TOURNAMENT:
            db_table_tournaments.insert(tournament.get_instantiation_serialisation_tournament())
            # In each tournament we search all players
            for player in tournament.get_players_instantiation_list():
                db_table_players.insert(player.get_instantiation_serialisation_player(index))
            # In each tournament we search all rounds
            for round in tournament.get_round_list():
                db_table_rounds.insert(round.get_instantiation_serialisation_round(index))

            index += 1



        # db_tournaments.insert({'name': 'jhone', 'age': '10'})
        # print(db_tournaments.all())
