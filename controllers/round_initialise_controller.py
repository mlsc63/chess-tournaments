
class RoundInitialiseController:
    def __init__(self, number_match, round_model):
        self.number_match = number_match
        self.round_model = round_model

    def __call__(self, *args, **kwargs):
        print('__Initailisation___')

        index = 0
        list_match = []

        while index != self.number_match:
            # One match contain in a tuple:
            #             (['Players Instantiation', 'score'], ['Players Instantiation', 'score'])
            match_tuple = (['', ''], ['', ''])
            list_match.append(match_tuple)
            print(str(self.round_model.get_name_round()))
            index += 1
        self.round_model.add_match_list(list_match)



















