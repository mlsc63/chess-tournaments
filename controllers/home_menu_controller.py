from models.menu_model import MenuModel
from views.menu_view import MenuView
from controllers.create_tournament_controller import CreateTournaments
from controllers.round_menu_controller import RoundMenuController
from controllers.data_controller import DataControllerErase, DataControllerLoad, DataControllerSave
from list import ListObjet
from controllers.information_board_controller import ListOfAllPlayersInATournament, ListOfAllPlayers,\
    ListOfAllTournaments, ListOfAllRoundsInATournament, ListOfAllMatchesInATournament


class HomeMenuController:
    """
    Works with menu_model and menu view for the menu display,
    three parameters are sent (Key entered by the user, the message displayed, and the function)
    We return the function associated with the key
    """
    def __init__(self):
        self.menu = MenuModel()
        self.view = MenuView(self.menu)


    def __call__(self):
        # We check if there is a tournament in progress
        print('___Acceuil___')

        # We check if save data exist
        if len(ListObjet.TOURNAMENT) == 0:
            data_controller_load = DataControllerLoad()
            data_controller_load()

        if len(ListObjet.TOURNAMENT) > 0:
            self.menu.add("auto", "Tournoi en cour", RoundMenuController())

        self.menu.add("auto", "Créer un tournois", CreateTournaments())
        self.menu.add("auto", "Liste de tous les acteurs d'un tournoi", ListOfAllPlayersInATournament())
        self.menu.add("auto", "Liste de tous les joueurs", ListOfAllPlayers())
        self.menu.add("auto", "Liste de tous les tournois", ListOfAllTournaments())
        self.menu.add("auto", "Liste de tous les tours d'un tournoi",  ListOfAllRoundsInATournament())
        self.menu.add("auto", "Liste de tous les matchs d'un tournoi", ListOfAllMatchesInATournament)
        self.menu.add("s", "Sauvegarder", DataControllerSave())
        self.menu.add('e', 'Effacer la base de donnée', DataControllerErase())
        self.menu.add("q", "Quitter)", lambda: None)

        user_choice = self.view.get_user_choice

        return user_choice
