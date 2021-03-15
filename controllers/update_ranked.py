class UpdateRanked:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        players_list = self.tournament.get_players_instantiation_list()
        print("___Mis à jour du classement de chaque joueurs___")
        for player in players_list:
            message = (str("Veuillez entrer le nouveau classement de " + player.get_name_p()))
            player.set_ranked(input(message))

        print("La mise à jour des scores est éfféctuée")

