from Card import Card
from TaskList import TaskList
class Board():
    def __init__(self, name):
        self.name = name
        self.task_lists = []

    def add_task_list(self, tasklist):
        self.task_lists.append(tasklist)

    def delete_task_list(self, name):
        found = False
        index = 0
        for tasklist in self.task_lists:
             if tasklist.name == name:
                 del self.task_lists[index]
                 found = True
                 break
             index += 1

        if not found:
            print(f"No task list found with the name '{name}'.")
    
    def move_task_list(self, from_index, to_index):
        if 0<= from_index < len(self.task_lists)