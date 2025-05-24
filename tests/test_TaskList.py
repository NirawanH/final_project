from src.TaskList import TaskList
from src.Card import Card

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

#Delete
def test_delete_card():
    task_list = TaskList("To do")
    card = Card("Homework")
    task_list.add_card(card)
    task_list.delete_card(card.id)
    assert card not in task_list.cards

#Move    

def test_move_card_to_another_list():
    card = Card("Test", "Detail")
    card.task_list = TaskList("In progress")
    card.target_list = TaskList("Done")
    assert card not in task_list
    assert card in target_list