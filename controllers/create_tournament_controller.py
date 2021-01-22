from controllers.validation_entries_controller import Entries
from models.tournament_model import TournamentsModel
from models.player_model import PlayerModel
from models.round_model import RoundModel
from . import home_menu_controller
from list import ListObjet


class CreateTournaments:

    def __init__(self):
        self.validation = Entries()
        self.tournament_model = TournamentsModel()

    def __call__(self):
        print("___Creation d'un nouveau tournoi___")
        self.tournament_model.add_name_tournament(self.validation.name("Name:"))
        self.tournament_model.add_date_tournament(self.validation.date('Date:\n'))
        self.tournament_model.add_location_tournament(self.validation.tournament_location('Lieu:\n'))
        self.tournament_model.add_number_of_turns_tournament(self.validation.tournament_number_of_turns('Nombre de tours:\n'))
        self.tournament_model.add_time_controller_tournament(self.validation.tournaments_time_controller('Contrôle du temps:\n'))
        self.tournament_model.add_number_of_players_tournament(self.validation.number('Nombre de participants (Nombre pair):\n'))
        self.tournament_model.add_description_tournament(self.validation.tournaments_descriptions('Description (option'))
        # save tournament in list
        ListObjet.TOURNAMENT.append(self.tournament_model)
        print(self.tournament_model)

        # add round

        rounds = 0
        while rounds != int(self.tournament_model.number_of_turns):
            round_model = RoundModel()
            round_model.add_name_round('Round ' + str(rounds))
            round_model.add_tournament_at_round(self.tournament_model)
            # save round in list
            ListObjet.ROUND_LIST.append(round_model)
            self.tournament_model.add_round_list_tournament(round_model)
            print(round_model)

            rounds += 1

        # add player
        players = 0
        print("___Ajout des joueurs___")
        while players != int(self.tournament_model.number_of_players):
            player_model = PlayerModel()
            player_model.add_first_name_player(self.validation.name('Prenom:'))
            player_model.add_name_player(self.validation.name('Nom:'))
            player_model.add_date_of_bird_player(self.validation.name(('Date de naissance')))
            player_model.add_sex_player(self.validation.sex('Sexe:'))
            player_model.add_ranked_player(self.validation.number('Niveau du joueur:'))
            player_model.add_tournament_player(self.tournament_model.get_name_tournament())
            # save player in list
            ListObjet.PLAYER.append(player_model)
            print(player_model)

            players += 1

        return home_menu_controller.HomeMenuController()
