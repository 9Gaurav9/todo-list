# Todo List App
#### Description:

The Todo List App is a simple yet functional command-line application designed to help users manage their tasks efficiently. This project demonstrates fundamental programming concepts in Python, including function definitions, user input handling, list operations, and unit testing with pytest.

## Project Structure

The project consists of the following files:

- **project.py**: This is the main file that contains the core logic of the Todo List App. It includes the main function which serves as the entry point of the application and three additional functions (`add_task`, `remove_task`, and `view_tasks`) that handle task management operations.
- **test_project.py**: This file contains unit tests for the three main functions in `project.py`. It uses the pytest framework to ensure that each function works as expected.
- **requirements.txt**: This file lists the dependencies required to run the tests for this project. In this case, it specifies the `pytest` library.
- **README.md**: This file provides a detailed description of the project, including its purpose, how to run it, and how it is structured.

## Detailed Description

### project.py

The `project.py` file contains the following functions:

- **main**: The main function serves as the entry point of the application. It presents a menu to the user with options to add, remove, view tasks, or exit the application. Based on the user's choice, it calls the appropriate function to perform the desired action.

- **add_task(task)**: This function takes a task as input and adds it to the `tasks` list. It prints a confirmation message once the task is added.

- **remove_task(task_id)**: This function removes a task from the `tasks` list based on the provided task ID. If the task ID is invalid, it prints an error message.

- **view_tasks**: This function prints all the tasks currently in the `tasks` list. If there are no tasks, it informs the user that the list is empty.

### test_project.py

The `test_project.py` file contains unit tests for the functions in `project.py`. Each test function is designed to test a specific aspect of the corresponding function to ensure it behaves correctly:

- **test_add_task**: Tests the `add_task` function by adding a task and checking if it is present in the `tasks` list.
- **test_remove_task**: Tests the `remove_task` function by adding two tasks, removing one, and checking if the correct task remains in the `tasks` list.
- **test_view_tasks**: Tests the `view_tasks` function by capturing its output and verifying that the correct tasks are displayed.

### requirements.txt

The `requirements.txt` file lists the dependencies needed to run the tests. It includes:
- `pytest`: A framework for writing simple and scalable test cases in Python.

## How to Run the Project

1. **Clone the repository**:
  git clone <https://github.com/9Gaurav9/todo-list>
   $ cd todo-list
2. **Install the requirements**:
3. **Run the application**:
4. **Run the tests**:


## Design Choices

The design of the Todo List App is intentionally kept simple to focus on demonstrating core programming concepts. The decision to use a command-line interface allows for straightforward user input handling and interaction. The tasks are stored in a list for easy manipulation, and the functions are designed to be clear and concise.

For testing, pytest was chosen due to its simplicity and powerful features for writing and running tests. Each test function is designed to be independent and focuses on a single functionality, making it easier to identify and fix issues.

Overall, the Todo List App is a practical project that illustrates how to build a basic Python application, handle user input, manage a list of items, and write unit tests to ensure the correctness of the program.


