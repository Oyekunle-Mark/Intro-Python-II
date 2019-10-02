# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    items = []

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def add_item(self, item):
        self.items.append(item)

    def item_exist(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True

        return False

    def remove_item(self, item_name):
        new_items = []

        for item in self.items:
            if item.name == item_name:
                removed_item = item
            else:
                new_items.append(item)

        self.items = new_items
        return removed_item

    def show_inventory(self):
        if len(self.items) > 0:
            print("Your inventory:")

            for item in self.items:
                print("  - ", item)
        else:
            print("Your inventory is empty.")

    def __str__(self):
        return f"Player {self.name} is in room {self.current_room}"

    def __repr__(self):
        return f"{self.name}, {self.current_room}"
