import datetime


class Entries:
    """
    Method used to verify user input. Returns the value if it is valid.
    """

    def name(self, msg):
        while True:
            print(msg)
            return_value = input()
            if len(return_value) >= 3:
                return return_value
            else:
                print("Veuillez insérer un nom valide")

    def date(self, msg):
        while True:
            print(msg)
            return_value = input()
            try:
                datetime.datetime.strptime(return_value, '%d/%m/%Y')
                return return_value
            except ValueError:
                print('Veuillez insérer une date valide')

    def tournament_location(self, msg):
        while True:
            print(msg)
            return_value = input()
            if len(return_value) >= 3:
                return return_value
            else:
                print("Veuillez insérer un lieu valide")

    def tournament_number_of_turns(self, msg):
        while True:
            print(msg)
            try:
                return_value = int(input())
                if return_value > 0:
                    return return_value
            except ValueError:
                print('Veuillez insérer un nombre de tours valide')

    def tournaments_time_controller(self, msg):
        while True:
            print(msg)
            return_value = input()
            if return_value == ('bullet' or 'blitz' or 'coup rapide'):
                return return_value
            else:
                print("Veuillez insérer un contrôlleur de"
                      " temps valide (bullet, blitz ou coup rapide)")

    def tournaments_descriptions(self, msg):
        while True:
            print(msg)
            return input()

    def sex(self, sex):
        while True:
            print(sex)
            return_value = input()
            if return_value == ('m' or 'f'):
                return return_value
            else:
                print("Veuillez insérer un sexe valide (f ou m)")

    def number_of_players(self, number):
        while True:
            print(number)
            try:
                return_value = int(input())
                if (return_value > 0) and (return_value % 2 == 0):
                    return return_value
            except ValueError:
                print('Veuillez insérer un nombre de joueurs pair')

    def player_level(self, number):
        while True:
            print(number)
            try:
                return_value = int(input())
                if return_value > 0:
                    return return_value
            except ValueError:
                print('Veuillez insérer un niveau valide')
