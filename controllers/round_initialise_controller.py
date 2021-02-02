
class RoundInitialiseController:
    def __init__(self, tournament, round_model):
        self.tournament = tournament
        self.round_model = round_model

    def first_init(self):
        print('__Initailisation___')

        numbers_of_match = (len(self.tournament.get_players_instantiation_list()) / 2)
        print(numbers_of_match)

        index = 0
        while index != numbers_of_match:
            match_tuple = ("", "", "")
            self.round_model.add_match_list(match_tuple)
            index += 1


        # if self.round_model.get_name_round() == "Round 1":



