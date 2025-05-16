from src.Card import Card
from datetime import date, datetime, timedelta
def test_Card():
    card = Card("dishes", "do the dishes!", date.today())
    assert card.title == "dishes"
    assert card.description == "do the dishes!"

 #editing title of the card       
    def test_edit_title():
        card = Card("No dishes")
        card.edit_description("Wash dishes")
        assert card.title == "Wash dishes"

#editing description of the card
    def test_edit_description():
        card = Card("Homework", "Old details" )
        card.edit_description("New details")
        assert card.description == "New details"

#Set deadline of the card
    def test_set_deadline():
        card = Card("Deadline")
        card.set_deadline(datetime.today)
        assert Card.deadline is not None
        assert Card.set_deadline() is True

#Deadline is valid or not
    def test_is_deadline_valid():
        card = Card("Expired")
        past_date = datetime.now() - timedelta(days=1)
        card.set_deadline(past_date.day, past_date.month, past_date.year, past_date.hour, past_date.minute)
        assert card.is_deadline_valid() is False
    
    def test_str_without_deadline(self):
        card = Card("Final project", "write a program")
        expected_output = (
            "Task: Learn Pytest \n"
            "Description: Testing __str__ method \n"
            "Deadline: No deadline"
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