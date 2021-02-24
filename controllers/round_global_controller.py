# TODO Finish the method
from views.matches_view import MatchesDisplay
from . import home_menu_controller
class MakeList:
    def __init__(self):
        self.player_list = ''
        self.round = ''
        self.tournament = ''
    def __call__(self, player_list, round):
        self.player_list = player_list
        self.round = round
        self.tournament = self.round.get_tournament_round()
        return_player_one_list = []
        return_player_two_list = []
        print(self.player_list)


        index = 0
        for player_id in self.player_list:
            # On enregistre le player un dans la liste de retour
            print('le premier joueur')

            return_player_one_list.append(player_list[0])

            # On veut savoir si cette adversaire a déjà joueur conter notre jouer 1
            position_adversaire = len(self.player_list) // 2
            while True:

                for meet in self.round.get_tournament_round().get_meet_tournament():
                    #####
                    print('meet[0] = ' + str(meet[0]) + ' == ' + str(self.player_list[position_adversaire]))
                    print('meet[0] = ' + str(meet[0]) + ' == ' + str(self.player_list[0]))
                    print('meet[1] = ' + str(meet[1]) + ' == ' + str(self.player_list[position_adversaire]))
                    print('meet[1] = ' + str(meet[1]) + ' == ' + str(self.player_list[0]))
                    if (((meet[0] == self.player_list[position_adversaire]) or (meet[0] == self.player_list[0])) and
                        ((meet[1] == self.player_list[position_adversaire]) or (meet[1] == self.player_list[0]))):

                        if len(player_list) <= (position_adversaire + 1):
                            print('Oui on peut aller chercher un adversaire +1')
                            position_adversaire += 1
                            break
                        else:
                            # mettre une condition quand on a fait le tours de tout les joueurs
                            print("Non il n'y a pas d'autre adversaire a la position + 1")
                            position_adversaire -= 1
                            break
                break

            print(self.player_list)
            print(index)
            print('le joueur 1 n a pas encore joué avec le player 2')
            return_player_two_list.append(self.player_list[position_adversaire])
            print('Je veux supptimer les id des joueurs ' + str(self.player_list[position_adversaire]) +
                  ' et ' + str(self.player_list[index]))

            del self.player_list[0]
            del self.player_list[position_adversaire - 1]
            print(str(self.player_list))
            print('List joueur 1' + str(return_player_one_list))
            print('list joueur 2' + str(return_player_two_list))

            if self.player_list == []:
                print('finisj')
                return return_player_one_list, return_player_two_list

            index += 1





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
                # On ajoute dans le tournois le meet pour avoir l'information dans les autres matchs

                self.round.get_tournament_round().set_meet_tournament([self.player_one[index].get_id_player(),
                                                                       self.player_two[index].get_id_player()])
                print(str(self.round.get_tournament_round().get_meet_tournament()))


                index += 1

            # On sauvegarde
            self.round.set_matches_list(matches_list)
            # On indique que le round est fini
            self.round.set_round_status_False()
            # on attrit les score

            return home_menu_controller.HomeMenuController()

        if self.round.get_name_round() != 'Round 1':
            score = self.round.get_tournament_round().get_score()
            # On trie les score pas odre croissant mais on récupére juste les index
            score_list = sorted(range(len(score)), key=lambda k: score[k])


            #####################
            make_list = MakeList()
            # self.player_one, self.player_two = make_list(score_list, self.round)
            self.player_one, self.player_two = make_list(score_list, self.round)
            index = 0
            matches_list = []
            print(str(self.player_one) + str(self.player_two))
            for match in self.round.get_match_list():

                matches_display = MatchesDisplay()
                score_player_one, score_player_two = matches_display(self.round.get_tournament_round().get_players_instantiation_list()[self.player_one[index]],
                                                                     self.round.get_tournament_round().get_players_instantiation_list()[self.player_two[index]])


                # On prépare la sauvergarde dans le match_tuple
                match_tuple = ([self.player_one[index], score_player_one],
                               [self.player_two[index], score_player_two])

                matches_list.append(match_tuple)
                self.set_score(score_player_one, int(self.player_one[index]),
                               score_player_two, int(self.player_two[index]),
                               self.round)
                # On ajoute dans le tournois le meet pour avoir l'information dans les autres matchs

                self.round.get_tournament_round().set_meet_tournament([self.player_one[index],
                                                                       self.player_two[index]])
                print(str(self.round.get_tournament_round().get_meet_tournament()))


                index += 1

            # On sauvegarde
            self.round.set_matches_list(matches_list)
            # On indique que le round est fini
            self.round.set_round_status_False()
            # on attrit les score

            return home_menu_controller.HomeMenuController()



