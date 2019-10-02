# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    items = []

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Player {self.name} is in room {self.current_room}"

    def __repr__(self):
        return f"{self.name}, {self.current_room}"
