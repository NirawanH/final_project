class TaskList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def delete_card(self, card_id):
        for card in self.cards:
            if card.id == card_id:
                self.cards.remove(card)
                print(f"Card ID {card_id} deleted.")
                return
        print("No card found.") 

    def move_card_to_another_list(self, card, target_list):
        if card in self.cards:
            self.cards.remove(card)
            target_list.add_card(card)

