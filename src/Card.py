from datetime import datetime

class Card:
    id_counter = 1
    def __init__(self, title: str, description: str = "", deadline = None):
        self.card_id = Card.id_counter
        Card.id_counter +=1
        self.title = str(title)
        self.description = str(description)
        self.deadline = deadline

#set deadline to str for JSON
        if isinstance(deadline, str): 
            self.set_deadline(deadline)
        elif isinstance(deadline, datetime):
            self.deadline = deadline

#editing title of the card       
    def edit_title(self, new_title: str):
        self.title = new_title

#editing description of the card
    def edit_description(self, new_description: str):
        self.description = new_description

#Set deadline of the card
    def set_deadline(self, date_str: str):
        for fmt in ("%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M", "%d-%m-%Y %H:%M" , "%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y"): #(DD/MM/YYYY HH:MM, YYYY-MM-DD HH:MM, DD-MM-YYYY HH:MM, YYYY-MM-DD, YYYY/MM/DD, DD/MM/YYYY, DD-MM-YYYY)
            try:
                self.deadline = datetime.strptime(date_str, fmt)
                return
            except ValueError:
                continue
        print("Invalid format. Please use DD/MM/YYYY HH:MM")
        self.deadline = None
            
    
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
    
    @staticmethod #group a function logically, does not need access to instance (self) or class (cls) variables or methods
    def from_dict(data):
        card = Card(data["title"], data["description"])
        card.card_id = data["card_id"]
        Card.id_counter = max(Card.id_counter, card.card_id +1) #next new card gets a unique ID
        if data["deadline"]:
            card.deadline = datetime.fromisoformat(data["deadline"])
        return card





        



