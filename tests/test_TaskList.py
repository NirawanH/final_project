import pytest
from src.TaskList import TaskList
from src.Card import Card

    
@pytest.fixture(autouse=True)
# Reset the card ID counter before each test
def reset_card_id():
    Card.id_counter = 1

def test_tasklist():
    task_list = TaskList("In progress")
    assert task_list.list_name == "In progress"
    assert task_list.cards == []

#Add
def test_add_card():
    task_list = TaskList("To do")
    card = Card("Final Project", "Learn Python")
    task_list.add_card(card)
    assert card in task_list.cards
    assert len(task_list.cards) == 1

#Delete
def test_remove_card():
    task_list = TaskList("To do")
    card1 = Card("Homework")
    card2 = Card("Homework2")
    task_list.add_card(card1)
    task_list.add_card(card2)
    task_list.remove_card(card2)
    assert card2 not in task_list.cards
    assert len(task_list.cards) == 1

#Get card 
def test_get_card():
    task_list = TaskList("To-do")
    card = Card("Test get card")
    task_list.add_card(card)
    result = task_list.get_card(card.card_id)
    assert result == card
    assert result is not None
    assert result.title == "Test get card"

def test_get_card_not_found():
    task_list = TaskList("To-do")
    result = task_list.get_card(3)
    assert result is None

    


