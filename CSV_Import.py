# import from CSV to data structures.
import csv
import io


def remove_zip(address):
    """ Takes as input an address with with a zip code at the end, returns the address without the zip code.

    :param address:
    :return: 
    """

    split_string = address.split()  # split address into words
    zip_removed_list = split_string[:-1]  # remove the last "word," which is the zip code.
    new_address = ' '.join([str(elem) for elem in zip_removed_list])  # convert list to string with list comprehension
    return new_address


def get_data_from_csv(input_csv):
    """
    This function goes through the given CSV files and puts each row into a single list, creating a 2D array
    Runtime:

    :param input_csv:
    :return:
    """

    csvfile = io.open(input_csv, mode='r', encoding='utf-8-sig')  # utf-8 spec required to remove chars at start
    readCSV = csv.reader(csvfile, delimiter=",")
    data_list = []
    for row in readCSV:
        data_list.append(row)
    return data_list
