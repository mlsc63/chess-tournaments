class MenuView:

    def __init__(self, menu):
        self.menu = menu

    def display(self):
        for key, entry in self.menu.entries.items():
            print(f"{key}:{entry.option}")

    def get_user_choice(self):
        self.display()
        while True:
            value = input(">>")
            for key in self.menu.entries.items():
                if key[0] == value:
                    return self.menu.entries[value].handler
            print("Non valide")
