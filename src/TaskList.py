from Card import Card
class TaskList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.cards = []
    
    def add_card(self, Card):
        self.cards.append(Card)

    def delete_card(self, id_card):
        for card in self.cards:
            if id_card == id_card:
                self.cards.remove(card)
                print(f"Card ID {id_card} deleted.")
                return
        print("No card found.") 

    def move_card_to_another_list(self, card, target_list):
        if card in self.cards:
            self.cards.remove(card)
            target_list.add_card(card)

