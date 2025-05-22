from Card import Card

class TaskList:
    def __init__(self, list_name: str):
        self.list_name = list_name
        self.cards = []
    
    def add_card(self, card: Card):
        self.cards.append(card)

    def delete_card(self, card_id: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.card_id == card_id:
                self.cards.remove(i)
                print(f"Card ID {card_id} deleted.")
                return True
        print("No card found.")
        return False 
    
    def get_card(self, card_id: str):
        for card in self.cards:
            if card.card_id == card_id:
                return card
        return None
    
    def list_card(self):
        if not self.cards:
            print(f"No cards in list '{self.list_name}'.")
        else:
            print(f"Cards in list '{self.list_name}'")
            for card in self.cards:
                print(f"- {card}")

