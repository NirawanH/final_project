from src.Card import Card
from src.TaskList import TaskList
from src.Board import Board

def show_all_cards(board):
    print("\n--- Your Task Board ---")
    for task_list in board.lists:
        print(f"\n== {task_list.list_name} ==")
        for card in task_list.cards:
            print(f"[{card.id}] {card.title} - {card.description}")
    print("-" * 40)

def main():
    board = Board()

    while True:
        print("\n📋 Task Management Menu")
        print("1. Add a Card")
        print("2. View All Cards")
        print("3. Move a Card")
        print("4. Delete a Card")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Card title: ")
            desc = input("Card description: ")
            card = Card(title, desc)
            board.lists[0].add_card(card)  # Add to "To-Do" by default
            print("✅ Card added to To-Do.")

        elif choice == "2":
            show_all_cards(board)

        elif choice == "3":
            card_id = int(input("Enter Card ID to move: "))
            from_list = input("Move from (To-Do / In Progress / Done): ")
            to_list = input("Move to (To-Do / In Progress / Done): ")
            board.move_card(card_id, from_list, to_list)

        elif choice == "4":
            card_id = int(input("Enter Card ID to delete: "))
            for task_list in board.lists:
                task_list.delete_card(card_id)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
