def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"


# print(__name__)
# if __name__ == "__main__":
#     print("hello")