# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project


import sys
import os
import ui  # User Interface
# Store module
from store import store
# Human Resources module
from hr import hr
# Tool manager module
from inventory import inventory
# Accounting module
from accounting import accounting
# Sales module
from sales import sales
# Customer Relationship Management (CRM) module
from crm import crm


def execute_function(options, pair_index):
    function_index = 1
    return options[pair_index][function_index]()


def choose(options):
    inputs = ui.get_inputs(["Please enter a number"], "")
    selected = inputs[0]
    try:
        selected = int(selected) - 1  # difference between index and printing options
        if selected == -1:
            return False
        execute_function(options, selected)
    except IndexError:
        ui.print_error_message('There is no such option')
    except ValueError:
        ui.print_error_message('There is no such option')
    return True


def main():
    options = [
        ("Store manager", store.start_module),
        ("Human resources manager", hr.start_module),
        ("Inventory manager", inventory.start_module),
        ("Accounting manager", accounting.start_module),
        ("Sales manager", sales.start_module),
        ("Customer Relationship Management (CRM)", crm.start_module),
    ]
    stay = True
    while stay:
        ui.print_menu("Main menu", options, "Exit program")
        try:
            stay = choose(options)
        except KeyError as err:
            ui.print_error_message(err)
    ui.clear()


if __name__ == '__main__':
    main()
