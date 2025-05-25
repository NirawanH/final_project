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

    def delete_task_list(self) -> bool:
        print("\nCurrent Task Lists:")
        if not self.task_lists:
            print("There is no list.")
            return False
    
        for i, task_list in enumerate(self.task_lists, start=1):
            print(f"{i}. {task_list.list_name}")

        try:
            index = int(input("Enter the number of the list to delete: "))
            if 1 <= index <= len(self.task_lists):
                selected_list = self.task_lists[index - 1]

                print(f"The list '{selected_list.list_name}' contains {len(task_list.cards)} card(s).")
                confirm = input("Are you sure you want to delete it? (y/n): ").lower()

                if confirm != "y":
                    print("Deletion cancelled.")
                    return False
                
                del self.task_lists[index-1]
                print(f"List '{selected_list.list_name}' deleted.")
                return True
            
            else:
                print("Invalid list number.")
                return False
            
        except ValueError:
            print("Please Enter a valid number.")
            return False


 
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
    
    def delete_card(self) -> bool:
        card_id = int(input("Enter card ID to delete: "))
        found_card = self.find_card(card_id)
        if found_card is not None:
            del found_card
            print(f"Card with ID {card_id} deleted.")
        else:
            print(f"No card with ID {card_id} found.")
    
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
    

    def __str__(self):
        output = [f"\n------- Board: {self.board_name} -------\n"]

        if not self.task_lists:
            output.append("- There is no task list and cards yet.")
            return "\n".join(output)

        for task_list in self.task_lists:
            output.append(f"- {task_list.list_name}")

            if not task_list.cards:
                output.append("  (No cards)")
                continue

            table = []
            for card in task_list.cards:
                if isinstance(card.deadline, str):
                    try:
                        card.deadline = datetime.fromisoformat(card.deadline)
                    except ValueError:
                        card.deadline = None

                # Format deadline with overdue warning
                if card.deadline:
                    if card.deadline < datetime.now():
                        deadline_str = "Overdue! " + card.deadline.strftime('%Y-%m-%d %H:%M')
                    else:
                        deadline_str = card.deadline.strftime('%Y-%m-%d %H:%M')
                else:
                    deadline_str = "None"

                table.append([card.card_id, card.title, card.description, deadline_str])

            output.append(tabulate(table, headers=["ID", "Title", "Description", "Deadline"], tablefmt="fancy_grid"))
        return "\n".join(output)    
    

board = Board()
print(board)