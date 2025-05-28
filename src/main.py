from Card import Card
from TaskList import TaskList
from Board import Board



def main():

    board = Board.load_from_file()

    while True:
        print("\n--- Wellcome to the board ---")
        print("1. View the board")
        print("2. Change board's name")
        print("3. Add a List")
        print("4. Edit a list name")
        print("5. Delete a List")
        print("6. Add a card")
        print("7. Edit a card")
        print("8. Delete a card")
        print("9. Move card to another list")
        print("10. Exit")

        choice = str(input("Choose an option (1-10): "))
        

        if choice == "1": #print("1. View the board")
            print(board)


        elif choice == "2": #print("2. Change board's name")
            print(f"Your current board name is {board.board_name}.\n")
            new_name = input("Enter new board name: ")
            board.change_board_name(new_name)
            print("Board name has been changed successfully!")
            print(board)
            board.save_to_file()


        elif choice == "3": #print("3. Add a List")
            print(board)
            list_name = str(input("Enter a new list name: "))
            board.add_task_list(TaskList(list_name))
            print(f"List '{list_name}' added.\n\n")
            print(board)
            board.save_to_file()

        elif choice == "4": #print("4. Edit a List name")
            board.edit_task_list()
            board.save_to_file()


        elif choice == "5": #print("5. Delete a List")
            board.delete_task_list()
            board.save_to_file()

   
        elif choice == "6": #print("6. Add a card")
            board.add_card_to_task_list()
            board.save_to_file()
                    
            
        elif choice == "7": #print("7. Edit a card")
            print(board)
            board.Edit_card_to_task_list()
            board.save_to_file()


        elif choice == "8": #print("8. Delete a card")
            print(board)
            board.delete_card()
            board.save_to_file()


        elif choice == "9": #print("9. Move card to another list")
            print(board)
            board.move_card()
            print(board)
            board.save_to_file()


        elif choice == "10":  #print("10. Exit")
            board.save_to_file()
            print("See you later!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 10.")

    print(board)

if __name__ == "__main__":
    main()
