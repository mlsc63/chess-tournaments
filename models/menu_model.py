class MenuEntry:


    def __init__(self, key, option, handler):
        self.option = option
        self.handler = handler
        self.key = key


class MenuModel:
    def __init__(self):
        self.autokey = 1
        self.entries = {}

    def add(self, key, option, handler=''):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

        self.entries[str(key)] = MenuEntry(key, option, handler)