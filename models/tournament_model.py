class TournamentsModel:

    def __init__(self, name='', location='', date='', number_of_turns=4,
                 time_controller='', number_of_players='', description='',
                 status=True, score=[], meet=[]):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_turns = number_of_turns
        self.time_controller = time_controller
        self.number_of_players = number_of_players
        self.description = description
        # Status --> for know if the tournament is done or not
        self.status = status
        self.round_list = []
        self.player_list = []
        self.score = score
        self.meet = meet

    # Set information of tournament

    def add_name_tournament(self, name):
        self.name = name

    def add_location_tournament(self, location):
        self.location = location

    def add_date_tournament(self, date):
        self.date = date

    def add_number_of_turns_tournament(self, number_of_turns):
        self.number_of_turns = number_of_turns

    def add_time_controller_tournament(self, time_controller):
        self.time_controller = time_controller

    def add_number_of_players_tournament(self, number_of_players):
        self.number_of_players = number_of_players

    def add_description_tournament(self, description=''):
        self.description = description

    def add_instantiation_players(self, instantiation):
        self.player_list.append(instantiation)

    def add_round_list_tournament(self, round):
        self.round_list.append(round)

    def add_score(self, score):
        self.score = score

    def get_players_instantiation_list(self):
        return self.player_list

    def get_name_tournament(self):
        return self.name

    def get_round_list(self):
        return self.round_list

    def get_status_tournament(self):
        return self.status

    def get_number_of_players(self):
        return self.number_of_players

    def get_instantiation_serialisation_tournament(self):
        return {'name': self.name,
                'location': self.location,
                'date': self.date,
                'number_of_turns': self.number_of_turns,
                'time_controller': self.time_controller,
                'number_of_players': self.number_of_players,
                'description': self.description,
                'status': self.status,
                'score': self.score,
                'meet': self.meet}

    def __repr__(self):
        return 'Tournois: {0}' \
               ' Lieu: {1} ' \
               'Date: {2} ' \
               'Nombre de tours: {3} ' \
               'Controle de temps: {4} ' \
               'Nombre de joueurs: {5} ' \
               'Description: {6}' \
               ''.format(self.name,
                         self.location,
                         self.date,
                         self.number_of_turns,
                         self.time_controller,
                         self.number_of_players,
                         self.description)

    def tournament_table(self):
        return [self.name, self.location, self.date, self.number_of_turns,
                self.time_controller, self.number_of_players, self.description,
                self.status]

    def set_score(self, id_player, score):
        self.score[id_player] += score

    def get_score(self):
        return self.score

    def set_meet_tournament(self, meet):
        self.meet.append(meet)

    def get_meet_tournament(self):
        return self.meet

    def get_tournament_turns(self):
        return self.number_of_turns

    def set_status_tournament_false(self):
        self.status = False
        print('Status false')

