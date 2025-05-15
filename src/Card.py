from datetime import datetime
class Card:
    id_card = 1
    def __init__(self, title, description= "", deadline = None):
        self.id = Card.id_card
        Card.id_card +=1
        self.title = title
        self.description = description
        self.deadline = deadline

 #editing title of the card       
    def edit_title(self, new_title):
        self.title = new_title

#editing description of the card
    def edit_description(self, new_description):
        self.description = new_description

#Set deadline of the card
    def set_deadline(self, day, month, year, hour=23, minute=59):
        self.deadline = datetime(year, month, day, hour, minute)

#Deadline is valid or not
    def is_deadline_valid(self):
        if self.deadline is None:
            return True
        return self.deadline > datetime.now()
    
#Set time left of the card        
    def time_left(self):
        if self.deadline:
            return self.deadline - datetime.now()
        return None
    
    def __str__(self):
        deadline_str = "No deadline" if self.deadline is None else self.deadline.strftime('%a %d-%b-%Y %H:%M')
        return f"Task: {self.title} \nDescription: {self.description} \nDeadline: {deadline_str}"
    
# task = Card("Complete project", "Finish the Python Assignment")    
# task.set_deadline(day=1, month=6, year=2025, hour=14)
# print(task)

if __name__ == "__main__":
    sample = Card("Example Task", "Just testing")
    sample.set_deadline(1, 6, 2025, 14)

    if not sample.is_deadline_valid():
        print("Deadline is already past!")
    else:
        print(sample)



        



