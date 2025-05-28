from Card import Card
from tabulate import tabulate

class TaskList:
    def __init__(self, list_name: str):
        self.list_name = list_name
        self.cards = [] #create list to collect card

    def edit_list_name(self, new_list_name: str):
        self.list_name = new_list_name
    
    def add_card(self, card: Card):
        self.cards.append(card) #add card to the list

    def remove_card(self, card: Card):
        self.cards.remove(card) #remove card from the list

    def get_card(self, card_id: int): #call card from card_id
        for card in self.cards:
            if card.card_id == card_id:
                return card
        return None


    def to_dict(self):
        return {
            "list_name" : self.list_name,
            "cards": [card.to_dict() for card in self.cards] #dict inside dict with for loop to collect card
        }
    
    @staticmethod
    def from_dict(data):
        task_list = TaskList(data["list_name"])
        task_list.cards = [Card.from_dict(card_data) for card_data in data["cards"]]
        return task_list
    
    

        