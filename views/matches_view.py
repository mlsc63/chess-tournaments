class MatchesDisplay:
    def __init__(self):
        pass

    def __call__(self, p_one, p_two):

        print(p_one.get_name_p() + ' VS ' + p_two.get_name_p())
        score_p_one = int(input('Entrer le score de ' + p_one.get_name_p()))
        score_p_two = int(input('Entrer le score de ' + p_two.get_name_p()))
        return score_p_one, score_p_two
