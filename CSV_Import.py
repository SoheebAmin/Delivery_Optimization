# import from CSV to data structures.
import csv
import io


def get_data_from_csv(input_csv):
    """
    :param input_csv: the location of a CSV file to be read
    :return: a 2D matrix that represents the rows and columns of the CSV
    Time Complexity: O(n)
    Space Complexity: O(n)

    This function goes through the given CSV files and puts each row into a single list, creating a 2D array
    """
    csv_file = io.open(input_csv, mode='r', encoding='utf-8-sig')  # utf-8 spec required to remove chars at start
    read_csv = csv.reader(csv_file, delimiter=",")  # reads the CSV file into a csv object
    data_list = []  # list to hold each row of pulled data
    for row in read_csv:  # iterate over the data
        data_list.append(row)  # append each row as a list within the list
    return data_list  # return the matrix of rows


def remove_zip(address):
    """
    :param address: an address that has as zip code at the end
    :return: The same address without the zip code at the end.
    Time Complexity: O(n)
    Space Complexity: O(n)

    Takes as input an address with with a zip code at the end, returns the address without the zip code.
    """
    split_string = address.split()  # split address into words
    zip_removed_list = split_string[:-1]  # remove the last "word," which is the zip code.
    new_address = ' '.join([str(elem) for elem in zip_removed_list])  # convert list to string with list comprehension
    return new_address
