# CLI Todo App (Hackathon AI-101 - P005)

## Short Description
A simple command-line interface (CLI) application built with Python to help users manage their daily tasks. It uses in-memory storage, which means tasks are lost when the program exits (Level 1 requirement).

## Features Implemented
* Add new tasks.
* View/List all tasks with their status.
* Mark tasks as complete or incomplete.
* Update/Edit an existing task title.
* Delete a task.

## How to Run the App

1.  Ensure you have Python installed.
2.  Save the files (`main.py`, `tasks.py`, `storage.py`) in the same directory (`todo-cli/`).
3.  Open your terminal or command prompt in that directory.
4.  Run the application using the following command:

    ```bash
    python main.py
    ```

## Bonus Features (Optional, based on your implementation)
*(If you implemented Level 2 storage, task priorities, or task filtering, list them here.)*

* Example: N/A (Currently using Level 1: In-Memory Storage)

## Use of Gemini CLI
Gemini CLI was used as an AI coding assistant throughout the development process. Specifically:

* **Initial Setup:** Gemini helped generate the boilerplate code for the first version of the main menu loop (`run_app` function) and the `display_menu` function.
* **Debugging:** The assistant was helpful in identifying and resolving a few `ValueError` issues related to casting user input (task IDs) to integers.
* **Code Review:** I used Gemini to review the `list_tasks` function for cleaner formatting and adherence to the required output style (`[ID] Title [Status]`).
