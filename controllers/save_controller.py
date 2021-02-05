from tinydb import TinyDB, Query
from  list import ListObjet

class SaveController:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        db_tournaments = TinyDB("db_tournaments.json")
        for i in ListObjet.TOURNAMENT:
            tournament_save = i.get_instantiation_serialisation()
            db_tournaments.insert(tournament_save)


        # db_tournaments.insert({'name': 'jhone', 'age': '10'})
        # print(db_tournaments.all())

