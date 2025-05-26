from src.Card import Card
from src.TaskList import TaskList
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

#Showing task_list inside task_lists 
    def get_list(self, list_name: str) -> TaskList or None:
        for task_list in self.task_lists:
            if task_list.list_name == list_name:
                return task_list
        return None

#Showing taks_list and card(with id)    
    def find_card(self, card_id: int) -> tuple[TaskList, Card] or tuple[None, None]:
        for task_list in self.task_lists:
            card = task_list.get_card(card_id)
            if card:
                return task_list, card
        return None, None
    
    def add_card_to_task_list(self) -> bool:
        print("\nCurrent Task Lists:")
        if not self.task_lists:
            print("---There is no list.---\n---Please add a list first.---")
            False

        else:
            for i, task_list in enumerate(self.task_lists):
                print(f"{i+1}. {task_list.list_name}")
                continue

        try:
            index = int(input("Enter the number of the list to add: "))
            if 1 <= index <= len(self.task_lists):
                selected_list = self.task_lists[index - 1]
                title = input("Enter card title: ")
                description = input("Enter card description: ")
                deadline = input("Enter deadline (optional: (YYYY-MM-DD HH:MM, leave blank to keep current)): ")
                card = Card(title, description, deadline)
                selected_list.add_card(card)
            
            else:
                print("Invalid list number.")
                return False
            
        except ValueError:
            print("Please Enter a valid number.")
            return False

        print(f"Card added with ID [{card.card_id}].")
        False        

#Working on this!!!
    def Edit_card_to_task_list(self) -> bool:
        choose_card_id = int(input("Enter card ID to edit: "))
        task_list, card = self.find_card(choose_card_id)
        if not card:
            print("Card not found.")
            False

        print(f"Editing card [{card.card_id}]: {card.title}")
        new_title = input("New title (leave blank to keep current): ")
        new_desc = input("New description (leave blank to keep current): ")
        new_deadline = input("New deadline (YYYY-MM-DD HH:MM, leave blank to keep current): ")

        if new_title:
            card.edit_title(new_title)
        if new_desc:
            card.edit_description(new_desc)
        if new_deadline:
            card.set_deadline(new_deadline)
        print("Card updated.")
 

    
    def delete_card(self) -> bool:
        card_id = int(input("Enter card ID to delete: "))
        found_card = self.find_card(card_id)
        if found_card is not None:
            del found_card
            print(f"Card with ID {card_id} deleted.")
        else:
            print(f"No card with ID {card_id} found.")
    
    def move_card(self) -> bool:
        #1. Choose card_id
        try:
            choose_card_id = int(input("Enter card ID to move: "))
        except ValueError:
            print("Please enter a valide card ID (number).")
            return False
        
        # Find the choosed card and the source list
        source_list, card = self.find_card(choose_card_id) 

        if not card:
            print(f"Card with ID {choose_card_id} not found.")
            return False
        
        print(f"Found card in list: '{source_list.list_name}'")


        #Show other task lists for selection (not show the source list)
        lists_to_choose = [
            (i, task_list) for i, task_list in enumerate(self.task_lists, start=1)
            if task_list != source_list
        ]
        
        if not lists_to_choose:
            print("No other lists available to move the card to.")
            return False
        
        print("\nAvailable List to move:")
        for i, task_list in lists_to_choose:
            print(f"{i}. {task_list.list_name}")

        try:
            index_of_target_list = int(input("Enter the number of the target list: "))
            for i, target_list in lists_to_choose:
                if index_of_target_list == i:
                    source_list.remove_card(card)
                    target_list.add_card(card)
                    print(f"Card '{card.title}' moved to list '{target_list.list_name}'.")
                    return True
                
            print("Invalide selections.")
            return False
        
        except ValueError:
            print("Please enter a valid number.")
            return False
        

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