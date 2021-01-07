# import from CSV to data structures.
import csv
import io


def get_data_from_csv(input_csv):
    """"This function goes through the given CSV files and puts each row into a single list, creating a 2D array
    Runtime: """

    csvfile = io.open(input_csv, mode='r', encoding='utf-8-sig')  # utf-8 spec required to remove chars at start
    readCSV = csv.reader(csvfile, delimiter=",")
    data_list = []
    for row in readCSV:
        data_list.append(row)
    return data_list

