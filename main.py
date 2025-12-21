todos = []

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
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
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('delete'):
        number = int(user_action[7:])
        print(number)

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index]
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print("byeee")


