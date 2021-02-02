class RoundGlobalController:
    def __init__(self, round):
        self.round = round

    def __call__(self, *args, **kwargs):

        # faire deux liste, 1 --> première motié, 2 ---> deuxième moitié
        # Si round 1 Mettre dans le tuple de match la permiere moitié vs la deuxième
        # SI round > 1 Mettre dans le tuple de match la permiere moitié vs la deuxième si ils n'ont jamias joué enssemble
        # Demander et enregistrer les scores.
        # Chnager le status du round -- > False
        # si c'est le dernier round, update score et changer le status du tournois --> False



        print('___Enregistrement des résultats___')

        # print(self.round.get_name_round())
        pass
