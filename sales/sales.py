# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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
PRICE_INDEX = 3
FILE_NAME = "sales/sales.csv"


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file(FILE_NAME)
    options = [
        ('Display table', lambda: display_table(table)),
        ('Add transaction', lambda: add(table)),
        ("Modify transaction data", lambda: update(table)),
        ("Remove transaction data", lambda: remove(table)),
        ("Display cheapest item", lambda: display_cheapest_item(table)),
        ("Display items sold between the dates", lambda: display_items(table)),
        ]
    stay = True
    while stay:
        ui.print_menu('Sales', options, 'Back to main menu')
        try:
            stay = common.choose(options, table)
        except KeyError as err:
            ui.print_error_message(err)
    data_manager.write_table_to_file(FILE_NAME, table)


def display_table(table):
    show_table(table)
    ui.pause()


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

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

def display_cheapest_item(table):
    pass


# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    names_and_ids = {}
    prices_and_names = {}
    lowest_price_list = []
    sorted_lowest_price_list = []
    lowest_price_list.append(table[0][PRICE_INDEX]) 

    for line in table:
        names_and_ids.update({line[NAME_INDEX]:line[ID_INDEX]})
        prices_and_names.update({line[PRICE_INDEX]:line[NAME_INDEX]})

    for line in table:
        if int(line[PRICE_INDEX]) < int(lowest_price_list[0]):
            old_price = lowest_price_list[0]
            lowest_price_list.append(int(line[PRICE_INDEX]))
            lowest_price_list.remove(old_price)

    if len(lowest_price_list) > 1:
        for i in lowest_price_list:
            smallest = min(prices_and_names[i])
            sorted_lowest_price_list.append(smallest)

    return str(names_and_ids[sorted_lowest_price_list[0]])


def display_items(table):
    pass


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table):
    # month_from, day_from, year_from, month_to, day_to, year_to
    pass
