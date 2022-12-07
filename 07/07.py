todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

            # [1]
            # new_todos = []
            #
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # [2]
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                # [3]
                item = item.strip('\n')
                row = f"[{index + 1}]-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")