class RoundGlobalController:
    def __init__(self, round):
        self.round = round

    def __call__(self, *args, **kwargs):

        if self.round.get_name_round() == 'Round 1':
            print('round 1')

            # Made in order players ranked increasing
            list_in_order = sorted(self.round.get_tournament_round().get_players_instantiation_list(),
                                   key=lambda player: player.ranked)
            for i in list_in_order:
                print(str(i))

            number_of_turn = int(len(list_in_order) / 2)

            list_adversaries = []
            index = 0
            while index != number_of_turn:
                list_adversaries.append(list_in_order.pop(number_of_turn))

            print(str(list_in_order))
            print(str(list_adversaries))

        # faire deux liste, 1 --> première motié, 2 ---> deuxième moitié
        # Si round 1 Mettre dans le tuple de match la permiere moitié vs la deuxième
        # SI round > 1 Mettre dans le tuple de match la permiere moitié vs la deuxième si ils n'ont jamias joué enssemble
        # Demander et enregistrer les scores.
        # Chnager le status du round -- > False
        # si c'est le dernier round, update score et changer le status du tournois --> False

        print('___Enregistrement des résultats___')

        # print(self.round.get_name_round())
        pass
