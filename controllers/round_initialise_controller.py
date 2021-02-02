
class RoundInitialiseController:
    def __init__(self, tournament, round_model):
        self.tournament = tournament
        self.round_model = round_model

    def __call__(self):
        print('__Initailisation___')

        for i in self.tournament.get_players_instantiation_list():
            match_tuple = (i, "", "")
            self.round_model.add_match_list(match_tuple)

        # if self.round_model.get_name_round() == "Round 1":



