import time


class RoundModel:
    def __init__(self):
        self.name = ''
        self.tournament = ''
        self.start_time = ''
        self.end_time = ''
        self.match_list = []
        # Status --> for know if the round is done or not
        self.status = True

    def add_name_round(self, name):
        self.name = name

    def add_start_time_round(self):
        self.start_time = time.strftime('%H:%M:%S')

    def add_end_time_round(self):
        self.end_time = time.strftime('%H:%M:%S')

    def add_match_list(self, match):
        self.match_list.append(match)

    # def add_tournament_at_round(self, tournament_at_round):
        # self.tournament = tournament_at_round

    def get_name_round(self):
        return self.name

    def get_match_list(self):
        return self.match_list

    def get_status_round(self):
        return self.status

    def __repr__(self):
        return 'Nom du round:{0}'.format(self.name)

