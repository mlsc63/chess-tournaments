from .home_menu_controller import HomeMenuController


class ApplicationController:
    """
    Receive a method, execute it, then start again
    """
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


