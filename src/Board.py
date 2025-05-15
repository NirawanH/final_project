from Card import Card
from TaskList import TaskList
class Board():
    def __init__(self):
        self.lists = [
            TaskList("To-Do"),
            TaskList("In Progress"),
            TaskList("Done")
        ]

    def move_card(self, card_id, from_list_name, to_list_name):
        from_list = next((l for l in self.lists if l.list_name == from_list_name), None)
        to_list = next((l for l in self.lists if l.list_name == to_list_name), None)

        if not from_list or not to_list:
            print("Invalid list name(s).")
            return

        for card in from_list.cards:
            if card.id == card_id:
                from_list.cards.remove(card)
                to_list.cards.append(card)
                print(f"Card ID {card_id} moved from {from_list_name} to {to_list_name}.")
                return

    print("Card not found.")
