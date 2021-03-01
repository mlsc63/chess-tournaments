from controllers.validation_entries_controller import Entries
from models.tournament_model import TournamentsModel
from models.player_model import PlayerModel
from models.round_model import RoundModel
from . import home_menu_controller
from list import ListObjet
from .round_initialise_controller import RoundInitialiseController


class CreateTournaments:
    """
    Creation of tournaments: Instantiation of tournaments, players, rounds.
    Contains player and round instantiations
    The instantiation of the tounois is saved in ListObjet
    Returns the menu function
    """

    def __init__(self):
        self.validation = Entries()
        self.tournament_model = TournamentsModel()
        self.player_model = ""
        self.round_model = ""

    def __call__(self):
        print("___Creation d'un nouveau tournoi___")
        self.tournament_model.add_name_tournament(
            self.validation.name(
                "Name:"))
        self.tournament_model.add_date_tournament(
            self.validation.date(
                'Date:\n'))
        self.tournament_model.add_location_tournament(
            self.validation.tournament_location(
                'Lieu:\n'))
        self.tournament_model.add_number_of_turns_tournament(
            self.validation.tournament_number_of_turns(
                'Nombre de tours:\n'))
        self.tournament_model.add_time_controller_tournament(
            self.validation.tournaments_time_controller(
                'Contrôle du temps:\n'))
        self.tournament_model.add_number_of_players_tournament(
            self.validation.number_of_players(
                'Nombre de participants (Nombre pair):\n'))
        self.tournament_model.add_description_tournament(
            self.validation.tournaments_descriptions(
                'Description (option)'))
        self.tournament_model.add_score(
            [0] * self.tournament_model.get_number_of_players())

        # save tournament in list
        ListObjet.TOURNAMENT.append(self.tournament_model)
        print(self.tournament_model)

        # add player
        id_players = 0
        print("___Ajout des joueurs___")
        while id_players != int(self.tournament_model.number_of_players):
            self.player_model = PlayerModel()
            self.player_model.add_first_name_player(
                self.validation.name('Prenom:'))
            self.player_model.add_name_player(
                self.validation.name('Nom:'))
            self.player_model.add_date_of_bird_player(
                self.validation.name(('Date de naissance')))
            self.player_model.add_sex_player(
                self.validation.sex('Sexe:'))
            self.player_model.add_ranked_player(
                self.validation.player_level('Niveau du joueur:'))
            self.player_model.add_id_player(id_players)

            # save instantiation in model of tournament
            self.tournament_model.add_instantiation_players(self.player_model)
            print(self.player_model)
            id_players += 1

        # add round
        rounds = 0
        while rounds != int(self.tournament_model.number_of_turns):
            self.round_model = RoundModel()
            self.round_model.add_name_round('Round ' + str(rounds + 1))
            self.round_model.add_tournament_at_round(self.tournament_model)

            # save round in list
            # ListObjet.ROUND_LIST.append(self.round_model)
            self.tournament_model.add_round_list_tournament(self.round_model)
            print(self.round_model)

            # Round initialisation
            numbers_of_match = (len(
                self.tournament_model.get_players_instantiation_list()) // 2)
            round_initialisation_controller = RoundInitialiseController(
                numbers_of_match, self.round_model)
            round_initialisation_controller()
            rounds += 1

            print(str(self.round_model.get_match_list()))

        return home_menu_controller.HomeMenuController()
