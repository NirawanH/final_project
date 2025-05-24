from datetime import datetime

class Card:
    id_counter = 1
    def __init__(self, title: str, description: str = "", deadline = None):
        self.card_id = Card.id_counter
        Card.id_counter +=1
        self.title = title
        self.description = description
        self.deadline = deadline

#editing title of the card       
    def edit_title(self, new_title: str):
        self.title = new_title

#editing description of the card
    def edit_description(self, new_description: str):
        self.description = new_description

#Set deadline of the card
    def set_deadline(self, date_str: str):
        try:
            self.deadline = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Invalid format. Please use DD/MM/YYYY HH:MM")

#Deadline is valid or not
    def is_deadline_valid(self):
        if self.deadline is None:
            return True
        elif self.deadline > datetime.now():
            return True
        else:
            return False
    
    def __str__(self):
        if self.deadline is None: 
            deadline_str = "No deadline" 
        else:
            deadline_str = self.deadline.strftime('%a %d-%b-%Y %H:%M')
            if self.deadline < datetime.now():
                deadline_str = "Overdue!!! " + self.deadline.strftime('%a %d-%b-%Y %H:%M')
        return f"{self.card_id}\nTask: {self.title}\nDescription: {self.description}\nDeadline: {deadline_str}"
    

    def to_dict(self):
        return {
            "card_id" : self.card_id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline.isoformat() if self.deadline else None
        }
    
    @staticmethod
    def from_dict(data):
        card = Card(data["title"], data["description"])
        card.card_id = data["card_id"]
        Card.id_counter = max(Card.id_counter, card.card_id +1)
        if data["deadline"]:
            card.deadline = datetime.fromisoformat(data["deadline"])
        return card



# card = Card("Final Project", "create an app")
# deadline = card.set_deadline(19,5,2025)
# print(card)



        



