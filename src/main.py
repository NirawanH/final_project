from Card import Card
from TaskList import TaskList
from Board import Board

board = Board.load_from_file()

def main():

    board = Board("My Board")

    while True:
        print("\nWellcome to the board")
        print("1. View the board")
        print("2. Change board's name")
        print("3. Add a List")
        print("4. Delete a List")
        print("5. Add a card")
        print("6. Edit a card")
        print("7. Delete a card")
        print("8. Move card to another list")
        print("9. Exit")

        choice = str(input("Choose an option (1-8): "))
        
        if choice == "1": #print("1. View the board")
            board.view_board()

        elif choice == "2": #print("2. Change board's name")
            print(f"Your current board name is {board.board_name}.\n")
            new_name = input("Enter new board name: ")
            board.change_board_name(new_name)

        elif choice== "3": #print("3. Add a List")
            print("\nCurrent Task Lists:")
            if not board.get_list():
                print("There is no list.")
            else:
                for i, task_list in enumerate(board.task_lists):
                    print(f"{i+1}. {task_list.list_name}")
            list_name = input(str("Enter new list name: "))
            if board.get_list(list_name):
                print("List already exists.")
            else:
                board.add_task_list(TaskList(list_name))
                print(f"List '{list_name}' added.")
                for list in task_list:
                    print(f"The current list name(s) is/are as follows: \n-{list}")
                    

        elif choice == "4": #print("4. Delete a List")
            print("\nCurrent Task Lists:")
            if not board.task_lists:
                print("There is no list.")
            else:
                for i, task_list in enumerate(board.task_lists):
                    print(f"{i+1}. {task_list.list_name}")
                try:
                    index = int(input("Enter the number of the list to delete: "))
                    if 1 <= index <= len(board.task_lists):
                        list_name = board.task_lists[index-1].list_name
                        board.delete_task_list(list_name)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")

   
        elif choice == "5": #print("5. Add a card")
            task_list = board.get_list(list_name)
            if not task_list:
                print("List not found.")
                continue  
            if task_list:
                for list in task_list:
                    print(f"List name(s) to choose: \n{list}")
                    continue
            list_name = input("Enter the list name to add the card to: ")
            

            title = input("Enter card title: ")
            description = input("Enter card description: ")
            deadline = input("Enter deadline (optional: (YYYY-MM-DD HH:MM, leave blank to keep current)): ")
            card = Card(title, description, deadline)
            task_list.add_card(card)
            print(f"Card added with ID [{card.card_id}].")

        elif choice == "6": #print("6. Edit a card")
            card_id = int(input("Enter card ID to edit: "))
            task_list, card = board.find_card(card_id)
            if not card:
                print("Card not found.")
                continue

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

        elif choice == "7": #print("7. Delete a card")
            

        elif choice == "8": #print("8. Move card to another list")
            card_id = int(input("Enter card ID to move: "))
            source_name = input("Enter source list name: ")
            target_name = input("Enter target list name: ")
            success = board.move_card(card_id, source_name, target_name)
            if success:
                print("Card moved successfully.")
            else:
                print("Failed to move card.")


        elif choice == "9":  #print("9. Exit")
            print("Thank you for using the app! See you later!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 8.")
    board.view_board()

if __name__ == "__main__":
    main()
