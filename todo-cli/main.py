# main.py
from tasks import (add_task, list_tasks, mark_task_complete, 
                   update_task, delete_task)
from storage import tasks, next_id

# Menu structure [cite: 25, 32]
# 1. Add task
# 2. List tasks
# 3. Mark task complete
# 4. Update task
# 5. Delete task
# 0. Exit

# main.py

import tasks
import storage

# --- Menu and Utility Functions ---

def display_menu():
    """Prints the main menu to the console."""
    print("\n==== TODO APP ====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task complete/incomplete")
    print("4. Update task title")
    print("5. Delete task")
    print("0. Exit")
    print("==================")

def run_app():
    """The main application loop."""
    # We use storage.tasks as the mutable list for all operations
    task_list = storage.tasks

    while True:
        display_menu()
        
        try:
            choice = input("Choose an option: ").strip()
        except EOFError:
            # Handle Ctrl+D or other termination signals gracefully
            print("\nExiting Todo App. Goodbye!")
            break
        
        # 1. Add task
        if choice == '1':
            print("\n--- ADD TASK ---")
            title = input("Enter task title: ").strip()
            if title:
                # next_id is managed internally by tasks.add_task via storage.py
                tasks.add_task(task_list, title)
            else:
                print("Task title cannot be empty.")

        # 2. List tasks
        elif choice == '2':
            tasks.list_tasks(task_list)

        # 3. Mark task complete/incomplete
        elif choice == '3':
            tasks.list_tasks(task_list)
            if task_list:
                task_id = input("Enter task ID to mark complete/incomplete: ").strip()
                tasks.mark_task_complete(task_list, task_id)
        
        # 4. Update task title
        elif choice == '4':
            tasks.list_tasks(task_list)
            if task_list:
                task_id = input("Enter task ID to update: ").strip()
                # Find task to show current title for better UX
                task = tasks.find_task_by_id(task_list, task_id)
                if task:
                    print(f"Current title: '{task['title']}'")
                    new_title = input("Enter new title (leave blank to cancel): ").strip()
                    if new_title:
                        tasks.update_task(task_list, task_id, new_title)
                    else:
                        print("Update cancelled.")
                else:
                    print(f"\nInvalid ID '{task_id}'. Task not found.")

        # 5. Delete task
        elif choice == '5':
            tasks.list_tasks(task_list)
            if task_list:
                task_id = input("Enter task ID to delete: ").strip()
                tasks.delete_task(task_list, task_id)
                
        # 0. Exit
        elif choice == '0':
            print("\nExiting Todo App. Goodbye!")
            break

        # Error Handling for invalid menu choice
        else:
            print("\nInvalid option, please try again.")


if __name__ == "__main__":
    run_app()

