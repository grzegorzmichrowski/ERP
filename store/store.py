# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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
TITLE = 2
MANUFACTURER = 3
PRICE = 4
IN_STOCK = 5
FILE_NAME = 'store/games.csv'


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
        ('Display games data', lambda: display_table(table)),
        ('Add new game data', lambda: add(table)),
        ("Modify games data", lambda: update(table)),
        ("Remove games data", lambda: remove(table)),
        ("Display number of types of games each manufacturer has", lambda: display_counts_by_manufacturers(table)),
        ("Display the average amount of games in stock of a given manufacturer",
         lambda: display_average_by_manufacturer(table)),
        ]
    stay = True
    while stay:
        ui.print_menu('Store manager', options, 'Back to main menu')
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
    labels = ['ID',
              'Full ID',
              'Title',
              'Manufacturer',
              'Price',
              'In stock']
    ui.print_table(table, labels)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    labels = ['Game title', 'Manufacturer', 'Price', 'Amount in stock']
    new_game_list = ui.get_inputs(labels, 'Adding new game to data')
    new_game_list.insert(0, common.generate_random(table))  # adding ID
    new_game_list.insert(0, str(len(table)+1))  # adding short ID

    if not common.is_positive_int(new_game_list[PRICE]):
        return table
    if not common.is_positive_int(new_game_list[IN_STOCK]):
        return table
    return table.append(new_game_list)


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
    id_ = ui.get_id()
    # get item by id
    # for each element in record: (excluding short id and full id:)
    # ask for new data
    # if new data is empty, do not update
    # else: update this data
    index = None
    for i, row in enumerate(table):
        if row[ID] == id_ or row[SHORT_ID] == id_:
            index = i
            break
    if index is not None:
        buffer = ui.update_element(table[index][TITLE], 'Game title')
        table[index][TITLE] = buffer.strip()
        buffer = ui.update_element(table[index][MANUFACTURER], 'Manufacturer name')
        table[index][MANUFACTURER] = buffer.strip()

        buffer = ui.update_element(table[index][PRICE], 'Price')
        if common.is_positive_int(buffer):
            table[index][PRICE] = buffer
        buffer = ui.update_element(table[index][IN_STOCK], 'Amount in stock')
        if common.is_positive_int(buffer):
            table[index][IN_STOCK] = buffer
    return table


def display_counts_by_manufacturers(table):
    pass


def manufacturers(table):
    manufacturers = []
    for line in table:
        if line[MANUFACTURER] not in manufacturers:
            manufacturers.append(line[MANUFACTURER])
    return manufacturers



manufacturers = manufacturers(data_manager.get_table_from_file(FILE_NAME))
# special functions:
# ------------------


# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturers_and_number_of_games = {}
    for i in range(len(manufacturers)):
        number_of_games = 1
        for line in table:
            if line[MANUFACTURER] == manufacturers[i]:
                manufacturers_and_number_of_games.update({manufacturers[i]: number_of_games})
                number_of_games += 1
    return manufacturers_and_number_of_games



def manufacturer_choice(manufacturers):
    inputs = ui.get_inputs(["Please enter a number"], "")
    options = int(inputs[0])
    manufacturer = manufacturers[options-1]
    if options > 0 and options <= len(manufacturers):
        return manufacturer
    elif options == 0:
        start_module()
    else:
        raise KeyError("There is no such option")
    return True



def choose_manufacturer(manufacturers):
    stay = True
    while stay:
        ui.print_menu('Manufacturers', manufacturers, 'Back to store manager')
        try:
            stay = manufacturer_choice(manufacturers)
        except KeyError as err:
            ui.print_error_message(err)

def display_average_by_manufacturer(table):
    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number


def get_average_by_manufacturer(table, manufacturer):
    amounts_of_games_in_stock = []
    for line in table:
        if line[MANUFACTURER] == manufacturer:
            amounts_of_games_in_stock.append(int(line[IN_STOCK]))
    _sum = 0
    for i in range(len(amounts_of_games_in_stock)):
        _sum += amounts_of_games_in_stock[i]
    average_amount_of_games = _sum // len(amounts_of_games_in_stock)
    avg_amount_of_games = str(average_amount_of_games)
    return avg_amount_of_games

    # your code
