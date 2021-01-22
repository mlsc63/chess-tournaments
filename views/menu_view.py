
class MenuView:

    def __init__(self, menu):
        self.menu = menu

    def display(self):
        print("___Acceuil___:")
        for key, entry in self.menu.entries.items():
            print(f"{key}:{entry.option}")

    def get_user_choice(self):
        self.display()

        value = input(">>")
        return self.menu.entries[value].handler