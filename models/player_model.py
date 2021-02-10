class PlayerModel:

    def __init__(self, first_name='', name='', date_of_bird="", sex='', ranked='', tournament=''):
        self.fist_name = first_name
        self.name = name
        self.date_of_bird = date_of_bird
        self.sex = sex
        self.ranked = ranked
        self.tournament = tournament

    def get_name_player(self):
        return self.name

    def add_first_name_player(self, first_name):
        self.fist_name = first_name

    def add_name_player(self, name):
        self.name = name

    def add_date_of_bird_player(self, date_of_bird):
        self.date_of_bird = date_of_bird

    def add_sex_player(self, sex):
        self.sex = sex

    def add_ranked_player(self, ranked):
        self.ranked = ranked

    # def add_tournament_player(self, tournament):
    # self.tournament = tournament
    def get_instantiation_serialisation_player(self, index):
        return {'index': index, 'first_name': self.fist_name, 'name': self.fist_name, 'date_of_bird': self.date_of_bird,
                'sex': self.sex, 'ranked': self.ranked}

    def __repr__(self):
        return 'Nom: {0} Prenom: {1} '.format(self.name, self.fist_name)

    def player_table(self):
        return [self.fist_name, self.name, self.date_of_bird, self.sex, self.ranked]
