# import from CSV to data structures.
import csv
import io

def remove_zip(string):
    """
    :param string:
    :return:
    """
    # split string
    spl_string = string.split()
    # remove the last item in list
    rm = spl_string[:-1]
    # convert list to string
    listToStr = ' '.join([str(elem) for elem in rm])
    return listToStr


def get_data_from_csv(input_csv, remove_zip=False):
    """
    This function goes through the given CSV files and puts each row into a single list, creating a 2D array
    Runtime:

    :param input_csv:
    :param remove_zip:
    :return:
    """

    csvfile = io.open(input_csv, mode='r', encoding='utf-8-sig')  # utf-8 spec required to remove chars at start
    readCSV = csv.reader(csvfile, delimiter=",")
    data_list = []
    for row in readCSV:
        if remove_zip:
            for item in row:
                print(item)
        data_list.append(row)
    return data_list

