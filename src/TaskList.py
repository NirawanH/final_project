from Card import Card
from tabulate import tabulate

class TaskList:
    def __init__(self, list_name: str):
        self.list_name = list_name
        self.cards = []
    
    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def get_card(self, card_id: int):
        for card in self.cards:
            if card.card_id == card_id:
                return card
        return None
    
    def list_card(self):
        if not self.cards:
            print(f"No cards in list '{self.list_name}'.")
            return
        
        table = []
        for card in self.cards:
            table.append([card.card_id, card.title, card.deadline, card.description])

        print(f"List: {self.list_name}")
        print(tabulate(table, headers=["ID", "Title", "Deadline", "Description"], tablefmt="grid"))


    # def to_dict(self):
    #     return {
    #         "list_name" : self.list_name,
    #         "cards": [card.to_dict() for card in self.cards]
    #     }
    
    # @staticmethod
    # def from_dict(data):
    #     task_list = TaskList(data["list_name"])
    #     task_list.cards = [Card.from_dict(card_data) for card_data in data["cards"]]
    #     return task_list
    
    
    # def debug_cards(self):
    #     for card in self.cards:
    #         print(f"Card ID: {card.card_id} \nTitle: {card.title}")
        