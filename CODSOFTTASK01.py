import sys
import os

def add_task(tasks, title, description):
    tasks.append({'title': title, 'description': description, 'completed': False})

def print_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        status = '[ ]' if not task['completed'] else '[x]'
        print(f'{i}. {status} {task["title"]}')
        if task['description']:
            print(f'   {task["description"]}')

def complete_task(tasks, task_number):
    try:
        tasks[task_number - 1]['completed'] = True
    except IndexError:
        print('Invalid task number.')

def report(tasks):
    completed = len([task for task in tasks if task['completed']])
    pending = len(tasks) - completed
    print(f'Completed tasks: {completed}')
    print(f'Pending tasks: {pending}')

def delete_task(tasks, task_number):
    try:
        del tasks[task_number - 1]
    except IndexError:
        print('Invalid task number.')

def main():
    if os.name == 'nt':
        os.system('title To-Do List')
    else:
        print('\033]2;To-Do List\007')

    tasks = []

    while True:
        command = input('\n(A)dd task, (P)rint tasks, (C)omplete task, (R)eport, (D)elete task, (Q)uit: ').upper()

        if command == 'A':
            title = input('Enter task title: ')
            description = input('Enter task descreption (optional): ')
            add_task(tasks, title, description)
        elif command == 'P':
            print_tasks(tasks)
        elif command == 'C':
            task_number = int(input('Enter task number to complete: '))
            complete_task(tasks, task_number)
        elif command == 'R':
            report(tasks)
        elif command == 'D':
            task_number = int(input('Enter task number to delete: '))
            delete_task(tasks, task_number)
        elif command == 'Q':
            sys.exit(0)
        else:
            print('Unknown command.')

if __name__ == '__main__':
    main()

