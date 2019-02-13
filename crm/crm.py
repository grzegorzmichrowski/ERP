# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
EMAIL_INDEX = 3
SUBSCRIBE_INDEX = 4
FILE_NAME = 'crm/customers.csv'


def choose():
    inputs = ui.get_inputs(["Please enter a number"], "")
    option = inputs[0]
    table = data_manager.get_table_from_file(FILE_NAME)
    common.add_short_id(table)
    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
    elif option == "3":
        update(table, ui.get_id()) # id_ z funkcji z common
    elif option == "4":
        table = remove(table, ui.get_id())
    elif option == "5":
        longest_name_id = get_longest_name_id(table)
        ui.print_result(longest_name_id, 'Longest name id\n')
    elif option == "6":
        newsletter_customers = get_subscribed_emails(table)
        ui.print_result(newsletter_customers, 'Customers with newsletter subscription\n')
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option")
    common.remove_short_id(table)
    data_manager.write_table_to_file(FILE_NAME, table)
    return True


def start_module():
    options = ['Display customers data',
                'Add new customer data',
                'Modify customers data',
                'Remove customers data',
                'Display id of the customer with the longest name',
                'Display email and name of customers that subscribed to the newsletter']
    stay = True
    while stay:
        ui.print_menu('Customer Relationship Management (CRM)', options, 'Back to main menu')
        try:
            stay = choose()
        except KeyError as err:
            ui.print_error_message(err)


    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file(FILE_NAME)
    options = [
        ('Display customers data', lambda: display_table(table)),
        ('Add new customer data', lambda: add(table)),
        ("Modify customers data", lambda: update(table)),
        ("Remove customers data", lambda: remove(table)),
        ("Display id of the customer with the longest name", lambda: display_longest_name_id(table)),
        ("Display email and name of customers that subscribed to the newsletter",
         lambda: display_subscribed_emails(table)),
        ]
    stay = True
    while stay:
        ui.print_menu('Customer Relationship Management (CRM)', options, 'Back to main menu')
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
              'Name',
              'E-mail',
              'Newsletter subscription']
    ui.print_table(table, labels)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    new_customer = ui.get_inputs(['Name', 'E-mail', 'Newsletter subscription'], 'Adding new customer to data')
    new_customer.insert(0, common.generate_random(table))
    new_customer.insert(0, str(len(table)))
    table.append(new_customer)
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
    id_ = ui.get_id()
    element_index = None
    for i, row in enumerate(table):
        if row[ID_INDEX] == id_ or row[SHORT_ID_INDEX] == id_:
            element_index = i
            break
    if element_index is not None:
        table[element_index][NAME_INDEX] = ui.update_element(table[element_index][NAME_INDEX], 'name')
        table[element_index][EMAIL_INDEX] = ui.update_element(table[element_index][EMAIL_INDEX], 'e-mail')
        table[element_index][SUBSCRIBE_INDEX] = ui.update_element(table[element_index][SUBSCRIBE_INDEX], 'newsletter subscription')
    return table


# special functions:
# ------------------
def display_longest_name_id(table):
    id_ = get_longest_name_id(table)
    ui.print_result(id_, 'ID of the customer with the longest name')


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):
    names_and_ids = {}
    for line in table:  # go through every line and add to dict name as key and id as value
        names_and_ids.update({line[NAME_INDEX]:line[ID_INDEX]})
    names_list = list(names_and_ids) # creates list with names 
    max_name_length = max(len(name) for name in names_list) # length of the longest name
    longest_length_names = [name for name in names_list if len(name) == max_name_length] # list of longest names
    first_in_alphabet = longest_length_names[0]
    for name in longest_length_names:
        if name < first_in_alphabet:
            first_in_alphabet = name
    id_ = names_and_ids[first_in_alphabet]
    return id_


def display_subscribed_emails(table):
    emails = get_subscribed_emails(table)
    ui.print_result(emails, 'These people has subscribed to the newsletter')


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    subscribed_newsletter_customers = []
    for line in table:
        if line[SUBSCRIBE_INDEX] == '1':
            email_and_name = line[EMAIL_INDEX]+';'+line[NAME_INDEX]
            subscribed_newsletter_customers.append(email_and_name)
    return subscribed_newsletter_customers
    # your code
