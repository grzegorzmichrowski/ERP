# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
MONTH_INDEX = 2
DAY_INDEX = 3
YEAR_INDEX = 4
OPERATION_INDEX = 5
AMOUNT_INDEX = 6
FILE_NAME = 'accounting/items.csv'
FUNCTION_INDEX = 1


# lista tupli, 1 element: drukowany podpis, 2 element: nazwa wywoływanej funkcji
OPTIONS = [
        ('Display accounting data', 'show_table'),
        ('Add new record', 'add'),
        ("Modify record", 'update'),
        ("Remove record", 'remove'),
        ("Display year with the highest frofit", 'which_year_max'),
        ("Display average profit in given year", 'avg_amount'),
        ]


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


def execute_function(function_name, table):
    return {
        'show_table': lambda: show_table(table),
        'add': lambda: add(table),
        'update': lambda: update(table),
        'remove': lambda: remove(table),
        'which_year_max': lambda: get_oldest_person(table),
        'avg_amount': lambda: get_persons_closest_to_average(table),
    }[function_name]()


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
        ui.print_menu('Accounting manager', OPTIONS, 'Back to main menu')
        try:
            stay = choose()
        except KeyError as err:
            ui.print_error_message(err)


def display_table(table):
    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    
    # your code

    labels = ['ID',
              'Full ID',
              'Month', 
              'Day', 
              'Year', 
              'Operation', 
              'Amount (USD)']
    ui.print_table(table, labels)


def is_operation(operation):
    try:
        if operation == 'in' or operation == 'out':
            return True
    except:
        ui.print_error_message(operation + ' is not an operation')
    return False


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    # your code
    labels = ['Month', 'Day', 'Year', 'Operation', 'Amount (USD)']
    new_record_list = ui.get_inputs(labels, 'Adding new record to data')
    new_record_list.insert(0, common.generate_random(table))  # adding ID
    new_record_list.insert(0, str(len(table)))  # adding short ID
    if not common.is_month(new_record_list[MONTH_INDEX]):
        return table
    if not common.is_day(new_record_list[DAY_INDEX], new_record_list[MONTH_INDEX]):
        return table
    if not common.is_positive_int(new_record_list[YEAR_INDEX]):
        return table
    if not is_operation(new_record_list[OPERATION_INDEX]):
        return table
    if not common.is_positive_int(new_record_list[AMOUNT_INDEX]):
        return table
    return table.append(new_record_list)


def remove(table):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code
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

    # your code

    return table


# special functions:
# ------------------


def display_year_max(table):
    pass

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


def display_average_profit(table):
    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
