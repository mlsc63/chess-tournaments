class MatchesDisplay:
    def __init__(self):
        pass

    def __call__(self, player_one, player_two):
        print(player_one.get_name_player() + ' VS ' +player_two.get_name_player())
        score_player_one = int(input('Entrer le score de ' + player_one.get_name_player()))
        score_player_two = int(input('Entrer le score de ' + player_two.get_name_player()))
        return score_player_one, score_player_two
