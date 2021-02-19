
class RoundInitialiseController:
    def __init__(self, number_match, round_model):
        self.number_match = number_match
        self.round_model = round_model

    def __call__(self, *args, **kwargs):
        index = 0
        list_match = []

        while index != self.number_match:
            match_tuple = (['', ''], ['', ''])
            list_match.append(match_tuple)
            index += 1
        self.round_model.add_match_list(list_match)



















