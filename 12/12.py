def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)



while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos("todo.txt")
        todos.append(todo + "\n")
        write_todos("todo.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todo.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"[{index + 1}]-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(f"{number} on todo list is being edited.")
            number = number - 1
            todos = get_todos("todo.txt")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos("todo.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("todo.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos("todo.txt", todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number!")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Wrong Command Entered.")

print("Bye!")