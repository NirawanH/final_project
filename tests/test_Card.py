from src.Card import Card
from src.TaskList import TaskList
from src.Board import Board
from datetime import date, datetime, timedelta
import pytest


#Test Card
def test_Card():
    card = Card("dishes", "do the dishes!")
    card.deadline = datetime(2025,5,25)
    assert card.title == "dishes"
    assert card.description == "do the dishes!"
    assert card.deadline == datetime(2025,5,25)

#Test title is str
def test_title_is_str():
    card = Card(222)
    assert isinstance(card.title, str)

#Test ID
def test_card_id():
    Card.id_counter = 1
    card1 = Card("One")
    card2 = Card("Two")
    assert card1.card_id == 1
    assert card2.card_id == 2

#Test desscription is ""
def test_card_default_description():
    card = Card("No description")
    assert card.description == ""

#Test editing title of the card       
def test_edit_title():
    card = Card("Eating")
    card.edit_title("Stop eating")
    assert card.title == "Stop eating"

#Test editing description of the card
def test_edit_description():
    card = Card("Homework", "Old details" )
    card.edit_description("New details")
    assert card.description == "New details"

#Test_Set deadline of the card
def test_set_deadline():
    card = Card("Final project", "create an app")
    card.set_deadline("01/05/2025 16:40")
    assert card.deadline is not None
    assert card.deadline.strftime("%d/%m/%Y %H:%M") == "01/05/2025 16:40"

def test_set_deadline_invalid_format():
    card = Card("OMG")
    card.set_deadline("24555")
    assert card.deadline is None


#Test string of the card    
def test_str_without_deadline():
    card = Card("Final project", "write a program")
    expected_output = (
        f"{card.card_id}\n"
        f"Task: Final project\n"
        f"Description: write a program\n"
        f"Deadline: No deadline"
    )
    assert str(card) == expected_output
    
def test_str_with_deadline():
    card = Card("Learn Python", "test datetime")
    card.set_deadline("1/6/2025 17:00")
    deadline_str = card.deadline.strftime('%a %d-%b-%Y %H:%M')
    expected_output = (
        f"{card.card_id}\n"
        f"Task: Learn Python\n"
        f"Description: test datetime\n"
        f"Deadline: {deadline_str}"
    )
    assert str(card) == expected_output

#Test to_dict()/ from_dict()
def test_card_to_from_dict():
    card = Card("Test", "Test Test")
    card.set_deadline("25/06/2025 11:00")
    data = card.to_dict()
    save = Card.from_dict(data)

    assert save.title == card.title
    assert save.description == card.description
    assert save.deadline == card.deadline
    assert save.card_id == card.card_id