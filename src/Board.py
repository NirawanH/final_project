from Card import Card
from TaskList import TaskList
from tabulate import tabulate
import json
from datetime import datetime


class Board():
    def __init__(self, board_name="My Board"): 
        self.board_name = board_name
        self.task_lists = []

    def change_board_name(self, new_board_name:str):
        self.board_name = new_board_name

    def add_task_list(self, task_list: TaskList):
        self.task_lists.append(task_list)

    def delete_task_list(self, list_name: str) -> bool:
        for i, task_list in enumerate(self.task_lists):
            if task_list.list_name == list_name:
                 print(f"The list '{list_name}' contains {len(task_list.cards)} card(s).")
                 confirm = input("Are you sure you want to delete it? (y/n): ").lower()
                 if confirm != "y":
                    print("Deletion cancelled.")
                    return False
            del self.task_lists[i]
            print(f"List '{list_name}' deleted.")
            return True
        print("List not found.")
        return False
    
    def view_board(self):
        print(f"\n\n\n=== Board: {self.board_name} ===")

        if not self.task_lists:
            print("No task lists available.")
            return

        for task_list in self.task_lists:
            print(f"\n--- {task_list.list_name} ---")

            if not task_list.cards:
                print("  (No cards)")
                continue

            table = []
            for card in task_list.cards:
                if isinstance(card.deadline, str):
                    card.deadline = datetime.fromisoformat(card.deadline)
                # Format deadline with overdue warning
                if card.deadline:
                    if card.deadline < datetime.now():
                        deadline_str = "Overdue! " + card.deadline.strftime('%Y-%m-%d %H:%M')
                    else:
                        deadline_str = card.deadline.strftime('%Y-%m-%d %H:%M')
                else:
                    deadline_str = "None"

                table.append([card.card_id, card.title, card.description, deadline_str])

            print(tabulate(table, headers=["ID", "Title", "Description", "Deadline"], tablefmt="fancy_grid"))
    
    def get_list(self, list_name: str) -> TaskList or None:
        for task_list in self.task_lists:
            if task_list.list_name == list_name:
                return task_list
        return None
    
    def find_card(self, card_id: int) -> tuple[TaskList, Card] or tuple[None, None]:
        for task_list in self.task_lists:
            card = task_list.get_card(card_id)
            if card:
                return task_list, card
        return None, None
    
    def move_card(self, card_id: int, source_list_name: str, target_list_name: str) -> bool:
        source_list = self.get_list(source_list_name)
        target_list = self.get_list(target_list_name)

        if not source_list or not target_list:
            print("One or both lists not found.")
            return False
        
        card= source_list.get_card(card_id)
        if not card:
            print("Card not found in the sorce list.")
            return False
        
        source_list.remove_card(card_id)
        target_list.add_card(card)
        return True
    
    def to_dict(self):
        return {
            "board_name": self.board_name,
            "task_list": [task_list.to_dict() for task_list in self.task_lists]
        }
    
    def from_dict(data):
        board = Board(data["board_name"])
        board.task_lists = [TaskList.from_dict(t) for t in data["task_lists"]]
        return board
    
    def save_to_file(self, filename="board_data.json"):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    
    def load_from_file(filename= "board_data.json"):
        try:
            with open(filename, "r") as f:
                date =  json.load(f)
                return Board.from_dict(data)
        except FileNotFoundError:
            print("No saved board found. Please create a new one.")
            return Board("My Board")