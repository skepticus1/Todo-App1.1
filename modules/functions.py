def get_todos(filepath="app1/files/todos.txt"):
    """
    Read a text file and return the list of todo items
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

#print(help(get_todos))

def write_todos(todos_arg, filepath="app1/files/todos.txt"):
    """ Write the todo items List in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos)
