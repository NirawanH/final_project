from Card import Card
from TaskList import TaskList
from Board import Board


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
        print("7. Move card to another list")
        print("8. Exit")

        choice = str(input("Choose an option (1-8): "))
        
        if choice == "1":
            board.view_board()

        elif choice == "2":
            new_name = input("Enter new board name: ")
            board.change_board_name(new_name)

        elif choice== "3":
            list_name = input(str("Enter new list name: "))
            if board.get_list(list_name):
                print("List already exists.")
            else:
                board.add_task_list(TaskList(list_name))
                print(f"List '{list_name}' added.")

        elif choice == "4":
            list_name = input("Enter the list name to delete: ")
            board.delete_task_list(list_name)

        elif choice == "5":
            list_name = input("Enter the list name to add the card to: ")
            task_list = board.get_list(list_name)
            if not task_list:
                print("List not found.")
                continue
            title = input("Enter card title: ")
            description = input("Enter card description: ")
            deadline = input("Enter deadline (optional): ")
            card = Card(title, description, deadline)
            task_list.add_card(card)
            print(f"Card added with ID [{card.card_id}].")

        elif choice == "6":
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

        elif choice == "7":
            card_id = int(input("Enter card ID to move: "))
            source_name = input("Enter source list name: ")
            target_name = input("Enter target list name: ")
            success = board.move_card(card_id, source_name, target_name)
            if success:
                print("Card moved successfully.")
            else:
                print("Failed to move card.")


        elif choice == "8":
            print("Thank you for using the app! See you later!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 8.")
    board.view_board()

if __name__ == "__main__":
    main()
