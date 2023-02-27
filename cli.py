# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('it is', now)
while True:
    # Get user input and strip space chars from it

    user_action = input("Type add,show,edit,delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        # Method-1
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # Method-2:context-manager
        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()
        todos = functions.get_todos()

        todos.append(todo + '\n')

        # Write todos in the file
        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")

            todos[number - 1] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not VALID")
            continue

    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])
            todos = functions.get_todos()

            deleted_todo = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)
            message = f"Todo:{deleted_todo} was deleted successfully"
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Enter the sr no of TODO")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("invalid")
print("bye")





