from item import Item


class Treasure(Item):
    is_treasure = True

    def __init__(self, name, description='a treasure!!!'):
        super().__init__(name)

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")

    def __str__(self):
        return "Treasure!!! " + super().__str__()
