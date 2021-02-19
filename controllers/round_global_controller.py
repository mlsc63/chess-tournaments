# TODO Finish the method
from views.matches_view import MatchesDisplay
from . import home_menu_controller


class SetScore:
    def __init__(self):
        self.score_player_one = ''
        self.id_player_one = ''
        self.score_player_two = ''
        self.id_player_two = ''
        self.tounament = ''

    def __call__(self, score_player_one, id_player_one, score_player_two, id_player_two, round):
        self.score_player_one = score_player_one
        self.id_player_one = id_player_one
        self.score_player_two = score_player_two
        self.id_player_two = id_player_two
        self.tounament = round.get_tournament_round()


        if score_player_one < score_player_two:
            self.tounament.set_score(id_player_one, 0)
            self.tounament.set_score(id_player_two, 1)
        if score_player_one > score_player_two:
            self.tounament.set_score(id_player_one, 1)
            self.tounament.set_score(id_player_two, 0)
        if score_player_one == score_player_two:
            self.tounament.set_score(id_player_one, 0.5)
            self.tounament.set_score(id_player_two, 0.5)





class RoundGlobalController:
    def __init__(self, round):
        self.round = round
        # Number of match
        self.numbers_of_match_in_round = len(self.round.get_tournament_round().get_players_instantiation_list()) // 2
        self.player_one = []
        self.player_two = []
        self.set_score = SetScore()

    def __call__(self, *args, **kwargs):

        if self.round.get_name_round() == 'Round 1':
            print(self.round.get_name_round())

            # Made in order players ranked increasing
            players_ranking_ascending = sorted(self.round.get_tournament_round().get_players_instantiation_list(),
                                               key=lambda player: player.ranked)

            # On traite tout les joueurs pour les mettre dans la liste player 1 ou 2
            index = 1
            for player_ranking in players_ranking_ascending:
                if index <= self.numbers_of_match_in_round:
                    self.player_one.append(player_ranking)
                else:
                    self.player_two.append(player_ranking)
                index += 1

            # On entre les scores, puis on les enregistre
            index = 0
            matches_list = []
            for match in self.round.get_match_list():
                # Affichage
                matches_display = MatchesDisplay()
                score_player_one, score_player_two = matches_display(self.player_one[index], self.player_two[index])

                # On prépare la sauvergarde dans le match_tuple
                match_tuple = ([self.player_one[index].get_id_player(), score_player_one],
                               [self.player_two[index].get_id_player(), score_player_two])
                matches_list.append(match_tuple)
                self.set_score(score_player_one, int(self.player_one[index].get_id_player()),
                               score_player_two, int(self.player_two[index].get_id_player()),
                               self.round)
                index += 1


            # On sauvegarde
            self.round.set_matches_list(matches_list)
            # On indique que le round est fini
            self.round.set_round_status_False()
            # on attrit les score

            return home_menu_controller.HomeMenuController()
