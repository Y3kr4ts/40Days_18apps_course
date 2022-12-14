todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"[{index + 1}]-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of todo to complete: "))

            with open('todo.txt', 'r') as file:
                file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break

print("Bye!")