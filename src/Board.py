from Card import Card
from TaskList import TaskList
from tabulate import tabulate

class Board():
    def __init__(self, board_name="My Board"):
        self.board_name = board_name
        self.task_lists = []

    def change_board_name(self, new_board_name:str):
        self.board_name = new_board_name

    def add_task_list(self, task_list: TaskList):
        self.task_lists.append(task_list)

    def delete_task_list(self, list_name: str) -> bool:
        for i, task_list in self.task_lists:
             if task_list.board_name == list_name:
                 del self.task_lists[i]
                 return True
        return False
    
    def move_task_list(self, from_index, to_index):
        if 0<= from_index < len(self.task_lists)