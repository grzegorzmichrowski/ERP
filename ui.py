import os

LABEL_INDEX = 0


def pause():
    print('\n\t', end='')
    input("Press ENTER...")


def get_longest_width(table, title, index):
    max_width = 0
    for t in table:
        if len(t[index]) > max_width:
            max_width = len(t[index])
    if len(title[index]) > max_width:
        max_width = len(title[index])
    return max_width


def calculate_width(list_of_widths):
    total = 0
    for l in list_of_widths:
        total += l
    total += len(list_of_widths)*2
    return total+len(list_of_widths)


def print_top_bar(width):
    print('/', end='')
    print('-'*width, end='')
    print('\\')


def print_bottom_bar(width):
    print('\\', end='')
    print('-'*width, end='')
    print('/')


def print_middle_bar(list_of_widths):
    print('|-', end='')
    for w in list_of_widths:
        print('-'*(w+2)+'|', end='')
    print()


def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/
    Args:
        table: list of lists - table to display
        title_list: list containing table headers
    Returns:
        This function doesn't return anything it only prints to console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')  # aby zadziałało musi wyspąpić 2 razy, dziwne
    number_of_rows = len(table[0])
    width = []  # zbyt ogólna nazwa
    for row in range(number_of_rows):
        width.append(get_longest_width(table, title_list, row))
    print_top_bar(calculate_width(width))
    print('|  ', end='')
    for i, column in enumerate(title_list):
        print('{:{}} | '.format(str(column), width[i]), end='')
    print()
    for row in table:
        print_middle_bar(width)
        print('|  ', end='')
        for i, column in enumerate(row):
            print('{:{}} | '.format(str(column), width[i]), end='')
        print()
    print_bottom_bar(calculate_width(width))


def print_result(result, label):
    """
    Displays results of the special functions.
    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result
    Returns:
        This function doesn't return anything it only prints to console.
    """
    print('\n\t'+label)
    if type(result) == str:
        print(result)
    elif type(result) == list:
        for r in result:
            print(r)
    elif type(result) == dict:
        for key in result:
            print(key, result[key])
    else:
        print(result)
    pause()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # aby zadziałało musi wyspąpić 2 razy, dziwne
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """
    clear()
    print(title+':')
    for index, option in enumerate(list_options):
        print('\t('+str(index+1)+') '+option[LABEL_INDEX])
    print('\t(0) '+exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    for i in list_labels:
        inputs.append(input(i+': '))
    return inputs


def update_element(old_data, label):
    new_data = input("New {}: ".format(label))
    if new_data == '':
        return old_data
    return new_data


def get_id():
    return input("Put full or short ID of element: ")


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message
    Args:
        message(str): error message to be displayed
    Returns:
        This function doesn't return anything it only prints to console.
    """
    print('\n\tError: '+str(message)+'\n')
    pause()
