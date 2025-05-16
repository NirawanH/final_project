from src.TaskList import TaskList
from src.Card import Card

def test_add_card():
    task_list = TaskList("In progress")
    card = Card("Final Project", "Learn Python")
    task_list.add_card(card)
    assert card in task_list.cards

def delete_card():
    task_list = TaskList("Done")
    card = Card("Homework")
    task_list.add_card(card)
    task_list.delete_card(card.id)
    assert card not in task_list.cards

def move_card_to_another_list(self, card, target_list):
    if card in self.cards:
        self.cards.remove(card)
        target_list.add_card(card)