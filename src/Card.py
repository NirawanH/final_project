from datetime import datetime

class Card:
    id_counter = 1
    def __init__(self, title: str, description: str, deadline = None):
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
            self.deadline = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD HH:MM")

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
    
# card = Card("Final Project", "create an app")
# deadline = card.set_deadline(19,5,2025)
# print(card)
     

        



