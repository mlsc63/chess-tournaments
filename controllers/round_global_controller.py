from views.matches_view import MatchesDisplay
from . import home_menu_controller
from .update_ranked import UpdateRanked
from views.data_table_view import DataTableView

class MakeList:
    """
    For rounds greater than one:
    Allows you to find an opponent for player one.
    They are already sorted in order of score.
     -If player one has already played with player two,
      we will check if the top player has not already played with.
     -If this is not possible we will check if there is a solution on
      the lower half.
     -If there is no solution then he will play with a player he has played
      with before.
    If there are two players left in the list then they will automatically
     play together
    """

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

        index = 0
        while self.player_list != []:
            for player_id in self.player_list:
                # We record player one in the return list
                return_player_one_list.append(player_list[0])
                # We want to know if this opponent has already
                # told our player 1
                position_adversaries = len(self.player_list) // 2
                position_adversaries_out_positive = False
                position_adversaries_out_negative = False

                # we find him an opponent
                while True:
                    for meet in self.round.get_tournament_round(). \
                            get_meet_tournament():

                        if (((meet[0]
                              == self.player_list[position_adversaries])
                             or (meet[0] ==
                                 self.player_list[0]))
                                and
                                ((meet[1]
                                  == self.player_list[position_adversaries])
                                 or (meet[1]
                                     == self.player_list[0]))):
                            print('Les deux adversaires ont déjà joué '
                                  'ensemble, essaie de trouver un '
                                  'autre adversaire')

                            # We anticipate and we see if we can have
                            # an opposing player has + or - possibilities
                            if not ((len(player_list) - 1) <=
                                    (position_adversaries + 1)):
                                position_adversaries_out_positive = True

                            if not (len(player_list)) > 1:
                                position_adversaries_out_negative = True
                            # If we have already scanned everything,
                            # that player 1 has already played with everyone,
                            # then he will play with the first person
                            # of the second half

                            if position_adversaries_out_negative and \
                                    position_adversaries_out_positive:
                                position_adversaries \
                                    = len(self.player_list) // 2
                                continue
                            if len(player_list) == 2:
                                # he plays together no choice
                                continue

                            else:

                                if (len(player_list) - 1) <= \
                                        (position_adversaries + 1):
                                    position_adversaries += 1
                                    break
                                else:
                                    # We do not find an opponent
                                    # by increasing the list
                                    position_adversaries_out_positive = True
                                    if len(player_list) > 1:
                                        print('on a fait toute la liste on'
                                              ' ne trouve pas d adversaire')
                                        position_adversaries -= 1

                                    break
                    break

                return_player_two_list \
                    .append(self.player_list[position_adversaries])
                del self.player_list[0]
                del self.player_list[position_adversaries - 1]
                index += 1

        return return_player_one_list, return_player_two_list


class Init:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        columns = ['Prenom', 'Nom', 'score']
        table_players = []
        index = []
        number_of_players = 1
        index_player = 0

        for score in self.tournament.get_score():
            player = self.tournament.get_players_instantiation_list()[index_player]

            table_players.append([player.get_first_name_p(), player.get_name_p(), score])
            index.append(number_of_players)
            number_of_players += 1
            index_player += 1

        DataTableView(table_players, index, columns).display()


class SetScore:
    def __init__(self):
        self.score_player_one = ''
        self.id_player_one = ''
        self.score_player_two = ''
        self.id_player_two = ''
        self.tounament = ''

    def __call__(self, score_player_one, id_player_one,
                 score_player_two, id_player_two, round):
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
    """
    Manage the first round:
     - Make two lists based on their ranking.
     A first list of players and a second adversary
    Manage player display and score feedback
    """

    def __init__(self, round):
        self.round = round
        # Number of match
        self.numbers_of_match_in_round = \
            len(self.round.get_tournament_round().
                get_players_instantiation_list()) // 2
        self.player_one = []
        self.player_two = []
        self.set_score = SetScore()

    def __call__(self, *args, **kwargs):

        if self.round.get_name_round() == 'Round 1':
            print(self.round.get_name_round())

            # Made in order players ranked increasing
            players_ranking_ascending = sorted(
                self.round.get_tournament_round()
                    .get_players_instantiation_list(),
                key=lambda player: player.ranked)

            # We treat all the players to put them in the player 1 or 2 list
            index = 1
            for player_ranking in players_ranking_ascending:
                if index <= self.numbers_of_match_in_round:
                    self.player_one.append(player_ranking)
                else:
                    self.player_two.append(player_ranking)
                index += 1

            # We enter the scores, then we record them
            index = 0
            matches_list = []
            for match in self.round.get_match_list():
                # Display
                matches_display = MatchesDisplay()
                score_player_one, score_player_two = matches_display(
                    self.player_one[index], self.player_two[index])

                # We prepare the save in the match tuple
                match_tuple = ([self.player_one[index].
                               get_id_player(), score_player_one],
                               [self.player_two[index].
                               get_id_player(), score_player_two])
                matches_list.append(match_tuple)
                self.set_score(score_player_one, int(self.player_one[index].
                                                     get_id_player()),
                               score_player_two, int(self.player_two[index].
                                                     get_id_player()),
                               self.round)
                # We add in the tournament the meet to have,
                # information in the other matches
                self.round.get_tournament_round().set_meet_tournament(
                    [self.player_one[index].get_id_player(),
                     self.player_two[index].get_id_player()])

                index += 1

            # We save
            self.round.set_matches_list(matches_list)
            # We indicate that the round is over
            self.round.set_round_status_False()
            # We attribute the scores

            # We check if it's the last round to pass the,
            # tournament in completed
            character_to_convert = self.round.get_name_round()[-1]
            converted_character = int(character_to_convert)

            if self.round.get_tournament_round() \
                    .get_tournament_turns() == converted_character:
                self.round.get_tournament_round().set_status_tournament_false()
            return home_menu_controller.HomeMenuController()

        if self.round.get_name_round() != 'Round 1':
            score = self.round.get_tournament_round().get_score()
            # We sort the score by increasing order but we just,
            # retrieve the indexes
            score_list = sorted(range(len(score)), key=lambda k: score[k])

            make_list = MakeList()
            self.player_one, self.player_two = make_list(
                score_list, self.round)
            index = 0
            matches_list = []

            for match in self.round.get_match_list():
                matches_display = MatchesDisplay()
                score_player_one, score_player_two = matches_display(
                    self.round.get_tournament_round()
                        .get_players_instantiation_list()
                    [self.player_one[index]],
                    self.round.get_tournament_round()
                        .get_players_instantiation_list()
                    [self.player_two[index]])

                # We prepare the save in the match_tuple
                match_tuple = ([self.player_one[index], score_player_one],
                               [self.player_two[index], score_player_two])

                matches_list.append(match_tuple)
                self.set_score(score_player_one, int(self.player_one[index]),
                               score_player_two, int(self.player_two[index]),
                               self.round)
                # We add in the tournament the meet to have information,
                # in the other matches
                self.round.get_tournament_round().set_meet_tournament(
                    [self.player_one[index], self.player_two[index]])

                index += 1

            # On save
            self.round.set_matches_list(matches_list)
            # We indicate that the round is over
            self.round.set_round_status_False()
            # we attribute the score

            # We check if it's the last round to pass the tournament,
            # in completed
            if self.round.get_tournament_round().get_tournament_turns() \
                    == int(self.round.get_name_round()[-1]):
                self.round.get_tournament_round().set_status_tournament_false()
                init = Init(self.round.get_tournament_round())
                init()
                update_ranked = UpdateRanked(self.round.get_tournament_round())
                update_ranked()

            return home_menu_controller.HomeMenuController()
