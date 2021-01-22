class TournamentsModel:

    def __init__(self, name='', location='', date='', number_of_turns='4', time_controller='', number_of_players='',
                 description=''):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_turns = number_of_turns
        self.time_controller = time_controller
        self.number_of_players = number_of_players
        self.description = description
        self.round_list = []

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

    def get_name_tournament(self):
        return self.name

    def add_round_list_tournament(self, round):
        self.round_list.append(round)

    def get_round(self):
        return self.round_list

    def __repr__(self):
        return 'Tournois: {0} Lieu: {1} Date: {2} Nombre de tours: {3} \
   Controle de temps: {4} Nombre de joueurs: {5} \
   Description: {6}'.format(self.name, self.location,
                            self.date, self.number_of_turns,
                            self.time_controller, self.number_of_players, self.description)
