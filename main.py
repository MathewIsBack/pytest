import time
from functions import get_todos, write_todos

todos = [] 

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos('todos.txt')

        todos.append(todo)

        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):

        todos = get_todos('todos.txt')
        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos('todos.txt', todos)

        except ValueError:
            print("Your command is not valid.")
            continue
            

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:])
            print(number)

            todos = get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos('todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print("byeee")


