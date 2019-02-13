# Do not modify this file
# Jeżeli ma to sens i będę w stanie to później obronić to mogę zmodyfikować


def add_short_id(table):
    index = 1
    for row in table:
        row.insert(0, str(index))
        index += 1
    return table


def remove_short_id(table):
    for row in table:
        del row[0]
    return table


def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    add_short_id(table)
    return table


# write a @table into a file
#
# @file_name: string
# @table: list of lists of strings
def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table: list of lists to write to a file

    Returns:
         None
    """
    remove_short_id(table)
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")
