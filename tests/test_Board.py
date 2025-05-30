import pytest
from src.Card import Card
from src.TaskList import TaskList
from src.Board import Board
from datetime import datetime

@pytest.fixture(autouse=True)
def reset_card_id():
    Card.id_counter = 1

#The testing:
# -Creating a board
def test_board_name():
    board = Board()
    assert board.board_name == "My Board"
    assert board.task_lists == []

def test_change_board_name():
    board = Board()
    board.change_board_name("Task Management")
    assert board.board_name == "Task Management"

# -Adding task lists
def test_add_task_list():
    board = Board()
    todo = TaskList("To-do")
    board.add_task_list(todo)
    assert len(board.task_lists) == 1
    assert board.task_lists[0].list_name == "To-do"

# -Getting a list
def test_get_list_found():
    board = Board()
    board.add_task_list(TaskList("To Do"))
    task_list = board.get_list("To Do")
    assert task_list is not None
    assert task_list.list_name == "To Do"    

def test_get_list_not_found():
    board = Board()
    assert board.get_list("Missing List") is None

# -Finding a card
def test_find_card():
    board = Board()
    todo = TaskList("To-do")
    card = Card("Python")
    todo.add_card(card)
    board.add_task_list(todo)

    found_list, found_card = board.find_card(card.card_id)
    assert found_list == todo
    assert found_card == card

def test_find_card_not_found():
    board = Board()
    todo = TaskList("To-do")
    todo, card = board.find_card(999)
    assert card is None

# -Moving cards between lists
def test_move_card():
    board = Board()
    todo = TaskList("To-do")
    done = TaskList("Done")
    board.add_task_list(todo)
    board.add_task_list(done)

    card = Card("Test")
    todo.add_card(card)

    # without input
    source_list, found_card = board.find_card(card.card_id)
    assert found_card == card

    source_list.cards.remove(card)
    done.add_card(card)

    assert card not in todo.cards
    assert card in done.cards

def test_to_dict():
    board = Board("My Projects")
    task_list1 = TaskList("To-do")
    board.add_task_list(task_list1)
    card = Card("Test", "Detail", "30/06/2025")
    task_list1.add_card(card)

    board_dict = board.to_dict()
    assert board_dict["board_name"] == "My Projects"
    assert len(board_dict["task_lists"]) == 1

    task_list_data = board_dict["task_lists"][0]
    assert task_list_data["list_name"] == "To-do"
    assert len(task_list_data["cards"]) == 1

    card_data = task_list_data["cards"][0]
    assert card_data["title"] == "Test"
    assert card_data["description"] == "Detail"
    assert card_data["deadline"] == card.deadline.isoformat()


def test_from_dict():
    board = Board("My Projects")
    task_list1 = TaskList("To-do")
    board.add_task_list(task_list1)
    task_list2 = TaskList("Doing")
    board.add_task_list(task_list2)

    old_board = board.to_dict()
    new_board = Board.from_dict(old_board)
    assert new_board.board_name == "My Projects"
    assert len(new_board.task_lists) == 2
    assert new_board.task_lists[0].list_name == "To-do"
    assert new_board.task_lists[1].list_name == "Doing"


