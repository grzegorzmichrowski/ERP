# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

SHORT_ID = 0
ID = 1
NAME = 2
MANUFACTURER = 3
DATE = 4
DURABILITY = 5
FILE_NAME = "inventory/inventory.csv"


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
        ('Display', lambda: display_table(table)),
        ('Add', lambda: add(table)),
        ("Modify", lambda: update(table)),
        ("Delete", lambda: remove(table)),
        ("Availability", lambda: display_available_items(table)),
        ("Average durability", lambda: display_average_durability_by_manufacturers(table)),
        ]
    stay = True
    while stay:
        ui.print_menu('Inventories', options, 'Back to main menu')
        try:
            stay = common.choose(options, table)
        except KeyError as err:
            ui.print_error_message(err)
    data_manager.write_table_to_file(FILE_NAME, table)


def show_table(table):
    """
    Display a table
    Args:
        table: list of lists to be displayed.
    Returns:
        None
    """
    labels = [
        'ID',
        'Full ID',
        'Item name',
        'Manufacturer',
        'Purchase date',
        'Durbility',
            ]
    ui.print_table(table, labels)


def display_table(table):
    show_table(table)
    ui.pause()


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    labels = ['Item name', 'Manufacturer', 'Purchase date', 'Durability (years)']
    new_item_list = ui.get_inputs(labels, 'Adding new item to data')
    new_item_list.insert(0, common.generate_random(table))  # adding ID
    new_item_list.insert(0, str(len(table)+1))  # adding short ID

    if not common.is_positive_int(new_item_list[DATE]):
        return table
    if not common.is_positive_int(new_item_list[DURABILITY]):
        return table
    return table.append(new_item_list)


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
        if row[ID] == id_ or row[SHORT_ID] == id_:
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
    index = common.find_by_id(table, ui.get_id())
    if index is not None:
        buffer = ui.update_element(table[index][NAME], 'Item name')
        table[index][NAME] = buffer.strip()
        buffer = ui.update_element(table[index][MANUFACTURER], 'Manufacturer name')
        table[index][MANUFACTURER] = buffer.strip()

        buffer = ui.update_element(table[index][DATE], 'Purchase date')
        if common.is_positive_int(buffer):
            table[index][DATE] = buffer
        buffer = ui.update_element(table[index][DURABILITY], 'Durability (years)')
        if common.is_positive_int(buffer):
            table[index][DURABILITY] = buffer
    return table


def display_available_items(table):
    pass


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists

def get_available_items(table):
    import datetime
    year_index=3
    durability_index=4
    d=datetime.datetime()
    year=d.year
    avability=[]
    for i, x in enumerate(table):
        if x[year_index]+x[durability_index]>=year:
            avability.append(table[i])
    return(avability)


def display_average_durability_by_manufacturers(table):
    pass


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    manufacturer_set=set()
    manufacturer=[]
    ava_durability={}
    for i, x in enumerate(table):
        manufacturer_set.add(x[manufacturer_index])
    for i in manufacturer_set:
        manufacturer.append(i)
    for i in range(len(manufacturer)):
        durability=[]
        _sum=0
        ava=0
        for line in table:
            if manufacturer[i] in line[manufacturer_index]:
                durability.append(int(line[durability_index]))
        for j in range(len(durability)):
            _sum+=durability[j]
        ava=float(_sum/len(durability))
        ava_durability.update({manufacturer[i]: ava})
    return ava_durability
