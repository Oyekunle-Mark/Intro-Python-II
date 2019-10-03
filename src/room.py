# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    n_to = None
    s_to = None
    e_to = None
    w_to = None

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def item_exist(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name:
                return True

        return False

    def remove_item(self, item_name):
        new_items = []

        for item in self.items:
            if item.name.lower() == item_name:
                removed_item = item
            else:
                new_items.append(item)

        self.items = new_items
        return removed_item

    def __str__(self):
        return f"In room {self.name}.\n{self.description}"

    def __repr__(self):
        return f"{self.name}, {self.description}"
