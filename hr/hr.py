# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

SHORT_ID_INDEX = 0
ID_INDEX = 1
NAME_INDEX = 2
AGE_INDEX = 3
FILE_NAME = "hr/persons.csv"
FUNCTION_INDEX = 1


# lista tupli, 1 element: drukowany podpis, 2 element: nazwa wywoływanej funkcji


# połączenie podpisów i nazw funkcji
OPTIONS = [
        ('Display table', 'show_table'),
        ('Add personal data', 'add'),
        ("Modify personal data", 'update'),
        ("Delete personal data", 'remove'),
        ("Display the oldest person", 'get_oldest_person'),
        ("Display people closest to average age", 'get_persons_closest_to_average'),
        ]


# source: https://stackoverflow.com/questions/23131594/choose-which-function-to-execute-based-on-a-parameter-its-name
def execute_function(function_name, table):
    return {
        'show_table': lambda: show_table(table),
        'add': lambda: add(table),
        'update': lambda: update(table),
        'remove': lambda: remove(table),
        'get_oldest_person': lambda: get_oldest_person(table),
        'get_persons_closest_to_average': lambda: get_persons_closest_to_average(table),
    }[function_name]()


def choose():
    inputs = ui.get_inputs(["Please enter a number"], "")
    option = inputs[0]
    table = data_manager.get_table_from_file(FILE_NAME)
    if option == '0':
        return False
    try:
        function_name = OPTIONS[int(option)-1][FUNCTION_INDEX]
        result = execute_function(function_name, table)
        if function_name == 'show_table':
            ui.pause()
        label = common.match_label(function_name)
        if label:
            ui.print_result(result, label)
    except IndexError:
        ui.print_error_message('There is no such option')
    except ValueError:
        ui.print_error_message('There is no such option')

    data_manager.write_table_to_file(FILE_NAME, table)
    return True


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.
    Returns:
        None
    """
    stay = True
    while stay:
        ui.print_menu("Human resources", OPTIONS, "Back to main menu")
        try:
            stay = choose()
        except KeyError as err:
            ui.print_error_message(err)


def show_table(table):
    """
    Display a table
    Args:
        table: list of lists to be displayed.
    Returns:
        None
    """
    labels = ['ID',
              'Full ID',
              'Name',
              'Year']
    ui.print_table(table, labels)


def add(table):
    """
    Asks user for input and adds it into the table.
    Args:
        table: table to add new record to
    Returns:
        Table with a new record
    """
    new_person_list = ui.get_inputs(['Name', 'Birth year'], 'Adding new person to data')
    new_person_list.insert(0, common.generate_random(table))  # adding ID
    new_person_list.insert(0, str(len(table)))  # adding short ID
    new_person_list[NAME_INDEX] = new_person_list[NAME_INDEX].strip()
    if common.is_year(new_person_list[AGE_INDEX]):
        table.append(new_person_list)
    return table


def remove(table):
    """
    Remove a record with a given id from the table.
    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed
    Returns:
        Table without specified record.
    """
    show_table(table)
    id_ = ui.get_id()
    for i, row in enumerate(table):
        if row[ID_INDEX] == id_ or row[SHORT_ID_INDEX] == id_:
            del table[i]
            return table
    return table


def update(table):
    """
    Updates specified record in the table. Ask users for new data.
    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
    Returns:
        table with updated record
    """
    show_table(table)
    id_ = ui.get_id()
    # get item by id
    # for each element in record: (excluding short id and full id:)
    # ask for new data
    # if new data is empty, do not update
    # else: update this data
    index = None
    for i, row in enumerate(table):
        if row[ID_INDEX] == id_ or row[SHORT_ID_INDEX] == id_:
            index = i
            break
    if index is not None:
        buffer = ui.update_element(table[index][NAME_INDEX], 'name')
        table[index][NAME_INDEX] = buffer.strip()
        buffer = ui.update_element(table[index][AGE_INDEX], 'birth year')
        if common.is_year(buffer):
            table[index][AGE_INDEX] = buffer
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    lowest_year = table[0][AGE_INDEX]
    for t in table:
        if t[AGE_INDEX] < lowest_year:
            lowest_year = t[AGE_INDEX]
    oldest_people = []
    for t in table:
        if t[AGE_INDEX] == lowest_year:
            oldest_people.append(t[NAME_INDEX])
    return oldest_people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def average_year(years_of_birth):
    numbers = years_of_birth
    return sum(numbers)/len(numbers)


def min_difference(numbers, average):
    min_ = abs(numbers[0] - average)
    for n in numbers:
        if abs(n - average) < min_:
            min_ = abs(n - average)
    return min_


def get_persons_closest_to_average(table):
    years_of_birth = []
    for row in table:
        years_of_birth.append(int(row[AGE_INDEX]))
    # wyznacz sredni rok urodzenia
    average = average_year(years_of_birth)
    # wyznacz najmniejsza roznice miedzy rokiem urodzenia a średnim rokiem urodzenia
    lowest_difference = min_difference(years_of_birth, average)
    # dodaj do listy wszystkie osoby o tej różnicy
    persons = []
    for t in table:
        if lowest_difference == abs(int(t[AGE_INDEX])-average):
            persons.append(t[NAME_INDEX])
    return persons
