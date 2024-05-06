def show_tasks():
    """
    This function display enumerated list of tasks or information if list is empty.
    :return: Enumerated list of tasks
    """
    if not todo_list:
        print('Todo list is empty.')
    else:
        for counter, task in enumerate(todo_list, 1):
            print(counter, task)


def add_task():
    """
    This function enable adding tasks to task list
    :return: Added task to tasks list
    """
    task_input = input('Enter task: ')
    todo_list.append(task_input)
    print('Task added successfully.')


def delete_task():
    """
    This function enable removing tasks by index and handles errors if index is incorrect.
    :return: Changed list of tasks
    """
    if not todo_list:
        print('Todo list is empty. Nothing to delete.')
    else:
        print('Current tasks:')
        for counter, task in enumerate(todo_list, 1):
            print(counter, task)
        try:
            index = int(input('Enter the index of the task to delete: '))
            if 1 <= index <= len(todo_list):
                del todo_list[index - 1]
                print('Task deleted successfully!')
            else:
                print('Invalid index.')
        except ValueError:
            print('Please enter a valid integer index.')


todo_list = []
while True:
    try:
        user_input = int(input('[1]: Show, [2]: Add, [3]: Delete '))
        if user_input == 1:
            show_tasks()
        elif user_input == 2:
            add_task()
        elif user_input == 3:
            delete_task()
        else:
            print('Incorrect value')
    except ValueError:
        print('Please enter a valid integer choice')
