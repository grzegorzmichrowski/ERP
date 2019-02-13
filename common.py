# implement commonly used functions here
import data_manager
import random
import string
import ui
ID_INDEX = 0
SHORT_ID = 0
FULL_ID = 1
# short index: skasowanie elementu w liście o konkretnym indeksie, no i to jest short id


# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
# inserts short ID (nr of row, starting from '1') at the beginning of row


def get_used_ids(table):
    used_id = []
    for row in table:
        used_id.append(row[ID_INDEX])
    return used_id


def choose2characters(word):
    border = len(word) - 1
    chosen = ''
    for i in range(2):
        chosen += word[random.randint(0, border)]
    return chosen


def create_random_id():
    id_characters = []
    special_characters = '!@#$%^&*><?'
    id_characters += choose2characters(special_characters)
    id_characters += choose2characters(string.digits)
    id_characters += choose2characters(string.ascii_lowercase)
    id_characters += choose2characters(string.ascii_uppercase)
    random.shuffle(id_characters)
    return ''.join(id_characters)


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """
    generated = table[0][ID_INDEX]
    taken_ids = get_used_ids(table)
    while generated in taken_ids:
        generated = create_random_id()
    return generated


def is_year(word):
    try:
        word = int(word)
        if word > 0:
            return True
        ui.print_error_message("Birth year is not a positive number")
        return False
    except:
        ui.print_error_message("Birth year is not a positive number")
        return False


def match_label(function_name):
    try:
        return {
            'get_oldest_person': 'Oldest people in base',
            'get_persons_closest_to_average': 'People closest to average',
        }[function_name]
    except KeyError:
        return False


# source: https://stackoverflow.com/questions/23131594/choose-which-function-to-execute-based-on-a-parameter-its-name
def execute_function(menu_options, selected_index, table):
    function_index = 1
    return menu_options[selected_index][function_index]()


def choose(options, table):
    inputs = ui.get_inputs(["Please enter a number"], "")
    try:
        selected = int(inputs[0])
        if selected == 0:
            return False
        execute_function(options, selected-1, table)
    except (IndexError):
        ui.print_error_message('There is no such option')
    return True


def is_month(word):
    try:
        month = int(word)
        if month > 0 and month < 13:
            return True
    except:
        ui.print_error_message(word + ' is not a month')
    return False


def is_day(word, month):
    feb = ['2']
    months_31_days = ['1', '3', '5', '7', '8', '10', '12']
    months_30_days = ['4', '6', '9', '11']
    try:
        day = int(word)
        if month in months_31_days and day > 0 and day < 32:
            return True
        if month in months_30_days and day > 0 and day < 31:
            return True
        if month in feb and day > 0 and day < 29:
            return True
    except:
        ui.print_error_message(word + ' is not a day')
    return False



def is_positive_int(word):
    try:
        number = int(word)
        if number > 0:
            return True
    except:
        ui.print_error_message(word + ' is not a positive number')
    return False


def find_by_id(table, id_):
    """
    returns None if element is not found
    """
    for i, row in enumerate(table):
        if row[FULL_ID] == id_ or row[SHORT_ID] == id_:
            return i
