from src.Card import Card
from datetime import date, datetime, timedelta


#1. Test class Card 
def test_Card():
    card = Card("dishes", "do the dishes!")
    card.deadline = datetime(20,5,2025)
    assert card.title == "dishes"
    assert card.description == "do the dishes!"
    assert card.deadline == datetime(20,5,2025)

#Test editing title of the card       
    def test_edit_title():
        card = Card("Eating")
        card.edit_description("Stop eating")
        assert card.title == "Stop eating"

#Test editing description of the card
    def test_edit_description():
        card = Card("Homework", "Old details" )
        card.edit_description("New details")
        assert card.description == "New details"

#Test_Set deadline of the card
    def test_set_deadline():
        card = Card("Final project", "create an app")
        card.set_deadline(datetime(1,5,2025))
        assert Card.deadline is not None
        assert Card.set_deadline() is True

#Deadline is valid or not (This case should show False)
    def test_is_deadline_valid():
        card = Card("Expired")
        past_date = datetime.now() - timedelta(days=1)
        card.set_deadline(past_date.day, past_date.month, past_date.year, past_date.hour, past_date.minute)
        assert card.is_deadline_valid() is False

#Test string of the card    
    def test_str_without_deadline(self):
        card = Card("Final project", "write a program")
        expected_output = (
            "Task: Final project \n"
            "Description: write a program \n"
            "Deadline: None"
        )
        assert str(card) == expected_output
    
    def test_str_with_deadline():
        card = Card("Learn Python", "datetime")
        card.set_deadline(20, 5, 2025, 14, 0)
        deadline_str = card.deadline.strftime('%a %d-%b-%Y %H:%M')
        expected_output = (
            f"Task: Learn Python \n"
            f"Description: datetime \n"
            f"Deadline: {deadline_str}"
        )
        assert str(card) == expected_output