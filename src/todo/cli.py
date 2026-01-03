from .service import TodoService

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Todo Application ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Mark Task Incomplete")
    print("5. Update Task")
    print("6. Delete Task ")
    print("7. Exit")
    print("--------------------")

def run_cli():
    """Runs the main command-line interface loop."""
    todo_service = TodoService()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter todo title (required): ")
            description = input("Enter todo description (optional): ")
            try:
                new_todo = todo_service.add_todo(title, description if description else None)
                print(f"Todo '{new_todo.title}' (ID: {new_todo.id}) added successfully!")
            except ValueError as e:
                print(f"Error adding todo: {e}")
        elif choice == '2':
            todos = todo_service.get_all_todos()
            if not todos:
                print("No todo items found.")
            else:
                print("\n--- Your Todo List ---")
                for todo in todos:
                    status = "✓" if todo.completed else " "
                    desc = f" - {todo.description}" if todo.description else ""
                    print(f"[{status}] ID: {todo.id} | Title: {todo.title}{desc}")
                print("--------------------")
        elif choice == '3':
            todo_id_str = input("Enter the ID of the todo to mark complete: ")
            try:
                todo_id = int(todo_id_str)
                if todo_service.mark_todo_complete(todo_id):
                    print(f"Todo with ID {todo_id} marked as complete.")
                else:
                    print(f"Todo with ID {todo_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a valid todo ID (a number).")
        elif choice == '4': # Implementation for Mark Task Incomplete
            todo_id_str = input("Enter the ID of the todo to mark incomplete: ")
            try:
                todo_id = int(todo_id_str)
                if todo_service.mark_todo_incomplete(todo_id):
                    print(f"Todo with ID {todo_id} marked as incomplete.")
                else:
                    print(f"Todo with ID {todo_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a valid todo ID (a number).")
        elif choice == '5':
            todo_id_str = input("Enter the ID of the todo to update: ")
            try:
                todo_id = int(todo_id_str)
                new_title = input("Enter new title (leave empty to keep current): ")
                new_description_input = input("Enter new description (leave empty to keep current, type 'clear' to remove): ")

                if new_title == "":
                    new_title = None # Don't update title
                
                if new_description_input == "":
                    new_description = None # Don't update description
                elif new_description_input.lower() == "clear":
                    new_description = "" # Clear description
                else:
                    new_description = new_description_input # Update with new value

                if todo_service.update_todo(todo_id, new_title, new_description):
                    print(f"Todo with ID {todo_id} updated successfully.")
                else:
                    print(f"Todo with ID {todo_id} not found or no changes provided.")
            except ValueError as e:
                print(f"Error updating todo: {e}")
        elif choice == '6':
            todo_id_str = input("Enter the ID of the todo to delete: ")
            try:
                todo_id = int(todo_id_str)
                if todo_service.delete_todo(todo_id):
                    print(f"Todo with ID {todo_id} deleted successfully.")
                else:
                    print(f"Todo with ID {todo_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a valid todo ID (a number).")
        elif choice == '7':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
