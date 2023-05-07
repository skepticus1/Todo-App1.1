from modules.functions import get_todos, write_todos
import time

date = time.strftime("%A, %d %b %Y %H:%M")
print(date)

while 2 > 1:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
        
    elif 'show' in user_action:
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            show = f"{index + 1}-{item}"
            print(show)
    
    elif 'edit' in user_action:
        try:
            number = int(user_action[5:])
            number -= 1
            todos = get_todos()
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print(f"The number {number + 1} isn't listed.")
            continue

    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])
            number -= 1
            todos = get_todos()
            todo_to_remove = todos[number].strip("\n").title()
            todos.pop(number)
            print(f"{todo_to_remove} has been removed from the list")
            write_todos(todos)
        
        except ValueError:
            print("Your command is not valid.")
            continue

    elif 'exit' in user_action:
        break
    
    else:
        print("You entered an unknown command")
    
print("Goodbye!")