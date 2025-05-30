from src.Card import Card
from src.TaskList import TaskList
from tabulate import tabulate
import json
import os
from datetime import datetime


class Board():
    def __init__(self, board_name="My Board"): 
        self.board_name = board_name
        self.task_lists = [] #create a list(task_lists) to store task_list

    def change_board_name(self, new_board_name:str):
        self.board_name = new_board_name

    def add_task_list(self, task_list: TaskList):
        self.task_lists.append(task_list)

    def edit_task_list(self) -> bool:
        print("\nCurrent Task Lists:")
        if not self.task_lists:
            print("There is no list.")
            return False
    
        for i, task_list in enumerate(self.task_lists, start=1):
            print(f"{i}. {task_list.list_name}")

        while True:
            try:
                index = int(input("Enter the number of the list to edit: "))
                if 1 <= index <= len(self.task_lists):
                    selected_list = self.task_lists[index - 1] #it needs to set to -1 because the real index start from 0 but the user will see it start from 1
                    print(f"The list name '{selected_list.list_name}' is selected")
                    new_list_name = str(input("Enter the new name to change: "))
                    
                    selected_list.edit_list_name(new_list_name)
                    print(f"The list name changed to '{new_list_name}")
                    return True
                
                else:
                    print("Invalid list number! Please try again.")
                
            except ValueError:
                print("Invalid number! Please Enter a valid number.")
    

    def delete_task_list(self) -> bool:
        print("\nCurrent Task Lists:")
        if not self.task_lists:
            print("There is no list.")
            return False
    
        for i, task_list in enumerate(self.task_lists, start=1):
            print(f"{i}. {task_list.list_name}")

        while True:
            try:
                index = int(input("Enter the number of the list to delete: "))
            except ValueError:
                print("Invalid list number! Please enter a valid number.")
                continue

            if 1 <= index <= len(self.task_lists):
                selected_list = self.task_lists[index - 1] #it needs to set to -1 because the real index start from 0 but the user will see it start from 1
                print(f"The list '{selected_list.list_name}' contains {len(task_list.cards)} card(s).")

                confirm = input("Are you sure you want to delete it? (y/n): ").lower()
                if confirm != "y":
                    print("Deletion cancelled.")
                    return False
                
                del self.task_lists[index-1] #it needs to set to -1 because the real index start from 0 but the user will see it start from 1
                print(f"List '{selected_list.list_name}' deleted.")
                return True
            
            print("Invalid list number. Please try again.")

                


#Showing task_list inside task_lists (maybe to improve this funtion later for filter, but now I am using enumerate)
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
        for i, task_list in enumerate(self.task_lists):
            print(f"{i+1}. {task_list.list_name}")

        if not self.task_lists:
            print("--- There are no task lists ---\n     --- Please add a list before adding a card ---")
            return False

        while True:
            try:
                index = int(input("Enter the number of the list to add: "))
            except ValueError:
                print("Invalid list number! Please enter a valid number.")
                continue

            if 1 <= index <= len(self.task_lists):
                selected_list = self.task_lists[index - 1]

                title = input("Enter card title: ")
                description = input("Enter card description, or leave blank: ")
                deadline = input("Enter deadline (optional: (DD/MM/YYYY HH:MM, leave blank to keep current)): ")
                card = Card(title, description, deadline)
                selected_list.add_card(card)
                print(f"Card added with ID [{card.card_id}].")
                return True 

            print("Invalid list number. Please try again.")
                



    def Edit_card_to_task_list(self) -> bool:
        while True:
            try:
                choose_card_id = int(input("Enter card ID to edit: "))

            except ValueError:
                print("Invalid card ID number! Please enter a valid card ID number.")
                continue

            task_list, card = self.find_card(choose_card_id)
            if not card:
                print("Card not found! Please enter a valid card ID number. ")
                continue

            deadline_str = card.deadline.strftime('%a %d/%m/%Y %H:%M') if card.deadline else None
            print(f"Editing card [{card.card_id}]: \n'Title:' {card.title}\n'Description:' {card.description}\n'Deadline: {deadline_str}'")

            new_title = input("New title (leave blank to keep current): ")
            new_desc = input("New description (leave blank to keep current): ")
            new_deadline = input("New deadline (DD/MM/YYYY HH:MM, leave blank to keep current): ")

            if new_title:
                card.edit_title(new_title)
            if new_desc:
                card.edit_description(new_desc)
            if new_deadline:
                card.set_deadline(new_deadline)

            print("Card updated.")
            return True


    
    def delete_card(self) -> bool:
        while True:
            try:
                card_id = int(input("Enter card ID to delete: "))

            except ValueError:
                print("Invalid card ID number! Please enter a valid card ID number.")
                continue

            task_list, card = self.find_card(card_id)

            if card:
                task_list.remove_card(card) 
                print(f"Card with ID {card_id} deleted.")
                return True
            else:
                print(f"No card with ID {card_id} found.")
                return False

    
    def move_card(self) -> bool:
        #1. Choose card_id
        while True:
            try:
                choose_card_id = int(input("Enter card ID to move: "))
            except ValueError:
                print("Invalid card ID number! Please enter a valide card ID (number).")
                continue
            
            # Find the choosed card and the source list
            source_list, card = self.find_card(choose_card_id) 

            if not card:
                print(f"Card with ID {choose_card_id} not found. Please enter a valide card ID (number)")
                continue

            print(f"Found card in list: '{source_list.list_name}'")
            break


        #Show other task lists for selection (not show the source list)
        lists_to_choose = [
            (i, task_list) for i, task_list in enumerate(self.task_lists, start=1)
            if task_list != source_list
        ]
        
        if not lists_to_choose:
            print("No other lists available to move the card to.")
            return False
        
        else:
            print("\nAvailable List to move:")
            for i, task_list in lists_to_choose:
                print(f"{i}. {task_list.list_name}")

            while True:
                try:
                    index_of_target_list = int(input("Enter the number of the target list: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                for i, target_list in lists_to_choose:
                    if index_of_target_list == i:
                        source_list.remove_card(card)
                        target_list.add_card(card)
                        print(f"Card ID [{card.card_id}] '{card.title}' moved to list '{target_list.list_name}'.")
                        return True
                    
                print("Invalid selection.")
            

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
                        deadline_str = "Overdue! " + card.deadline.strftime('%a %d/%m/%Y %H:%M')
                    else:
                        deadline_str = card.deadline.strftime('%a %d/%m/%Y %H:%M')
                else:
                    deadline_str = "None"

                table.append([card.card_id, card.title, card.description, deadline_str])

            output.append(tabulate(table, headers=["ID", "Title", "Description", "Deadline"], tablefmt="fancy_grid"))
        return "\n".join(output)    
    

    def to_dict(self):
        return {
            "board_name": self.board_name,
            "task_lists": [task_list.to_dict() for task_list in self.task_lists]
            }

    @staticmethod
    def from_dict(data):
        board = Board(data["board_name"])
        board.task_lists = [TaskList.from_dict(tl) for tl in data["task_lists"]]
        return board
    

    def save_to_file(self, filename="board_data.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)
        print(f"\n\nBoard saved to {filename}")

    @staticmethod
    def load_from_file(filename="board_data.json"):
        if not os.path.exists(filename):
            print("No saved board found.")
            return Board()
        
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Board.from_dict(data)

