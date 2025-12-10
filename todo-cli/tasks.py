
next_id = 1

def add_task(task_list: list, title: str):
    global next_id
    task = {
        'id': next_id,
        'title': title,
        'done': False
    }
    task_list.append(task)
    next_id += 1

# tasks.py

# We need to import the in-memory list and the ID counter from storage.py
# In a real application, 'next_id' might be managed differently, but for 
# this beginner hackathon, we'll keep it simple using the global from storage.
# We also need to import the storage module to modify the global 'next_id'.
import storage 

# --- Helper Function (Internal Use) ---

def find_task_by_id(tasks, task_id):
    """Searches the task list for a task with the given ID."""
    try:
        task_id = int(task_id)
    except ValueError:
        return None # Return None if ID is not a valid number
        
    for task in tasks:
        if task.get("id") == task_id:
            return task
    return None # Return None if no task is found

# --- Core Task Management Functions ---

def add_task(tasks, title):
    """
    Creates a new task dictionary and appends it to the tasks list.
    
    Args:
        tasks (list): The list where tasks are stored (e.g., storage.tasks).
        title (str): The title of the new task.
    """
    # Use and increment the global ID counter from the storage module
    task_id = storage.next_id
    storage.next_id += 1 

    new_task = {
        "id": task_id,
        "title": title,
        "done": False 
    }
    
    tasks.append(new_task)
    print(f"\nTask ID {task_id}: '{title}' added successfully. [cite: 96]")


def list_tasks(tasks):
    """
    Displays all tasks, showing ID, Title, and Status.
    
    Args:
        tasks (list): The list of task dictionaries.
    """
    if not tasks:
        print("\nNo tasks found. [cite: 97]")
        return
        
    print("\n==== Current Tasks ====")
    
    for task in tasks:
        # Determine the status string for display
        status = "[Done]" if task["done"] else "[Not Done]" # 
        
        # Format the output: [ID] Title Status
        print(f"[{task['id']}] {task['title']} {status}") # [cite: 44, 45]
        
    print("=======================")


def mark_task_complete(tasks, task_id_input):
    """
    Flips the 'done' status of a task identified by its ID. [cite: 53]
    
    Args:
        tasks (list): The list of task dictionaries.
        task_id_input (str): The ID entered by the user.
    """
    task = find_task_by_id(tasks, task_id_input)
    
    if task:
        # Flip the status
        task["done"] = not task["done"]
        
        new_status_str = "Complete" if task["done"] else "Incomplete"
        print(f"\nTask ID {task['id']} status updated to: {new_status_str}.")
    else:
        print(f"\nInvalid ID '{task_id_input}'. Task not found. ")


def update_task(tasks, task_id_input, new_title):
    """
    Allows the user to change the title of an existing task. [cite: 57]
    
    Args:
        tasks (list): The list of task dictionaries.
        task_id_input (str): The ID entered by the user.
        new_title (str): The new title for the task.
    """
    task = find_task_by_id(tasks, task_id_input)
    
    if task:
        old_title = task["title"]
        task["title"] = new_title
        print(f"\nTask ID {task['id']} updated.")
        print(f"  Old Title: '{old_title}'")
        print(f"  New Title: '{task['title']}'")
    else:
        print(f"\nInvalid ID '{task_id_input}'. Task not found. ")


def delete_task(tasks, task_id_input):
    """
    Removes a task from the list using its ID. [cite: 64]
    
    Args:
        tasks (list): The list of task dictionaries.
        task_id_input (str): The ID entered by the user.
    """
    task_to_delete = find_task_by_id(tasks, task_id_input)
    
    if task_to_delete:
        tasks.remove(task_to_delete) # Remove the dictionary object
        print(f"\nTask ID {task_to_delete['id']} ('{task_to_delete['title']}') deleted successfully. [cite: 65]")
    else:
        print(f"\nInvalid ID '{task_id_input}'. Task not found. ")
