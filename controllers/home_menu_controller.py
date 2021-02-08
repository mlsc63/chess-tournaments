from models.menu_model import MenuModel
from views.menu_view import MenuView
from controllers.create_tournament_controller import CreateTournaments
from controllers.round_menu_controller import RoundMenuController
from controllers.data_controller import DataControllerErase, DataControllerLoad, DataControllerSave
from list import ListObjet


class HomeMenuController:
    def __init__(self):
        self.menu = MenuModel()
        self.view = MenuView(self.menu)


    def __call__(self):
        # We check if there is a tournament in progress

        print('___Acceuil___')
        # We check if save data exist

        if len(ListObjet.TOURNAMENT) == 0:
            DataControllerLoad()


        if len(ListObjet.TOURNAMENT) > 0:
            self.menu.add("auto", "Tournoi en cour", RoundMenuController())

        self.menu.add("auto", "Créer un tournois", CreateTournaments())
        self.menu.add("auto", "Liste de tous les acteurs d'un tournoi", lambda: None)
        self.menu.add("auto", "Liste de tous les joueurs", lambda: None)
        self.menu.add("auto", "Liste de tous les tournois", lambda: None)
        self.menu.add("auto", "Liste de tous les tours d'un tournoi", lambda: None)
        self.menu.add("auto", "Liste de tous les matchs d'un tournoi", lambda: None)
        self.menu.add("s", "Sauvegarder", DataControllerSave())
        self.menu.add('e', 'Effacer la base de donnée', DataControllerErase())
        self.menu.add("q", "Quitter)", lambda: None)

        user_choice = self.view.get_user_choice

        return user_choice
