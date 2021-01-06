# import from CSV to data structures.
import csv
import io


def get_data_from_csv(packages_csv):
    """"This function goes through the given CSV files and puts each row into a single list, creating a 2D array
    Runtime: """

    csvfile = io.open(packages_CSV, mode='r', encoding='utf-8-sig')  # utf-8 spec required to remove chars at start
    readCSV = csv.reader(csvfile, delimiter=",")
    packages_data_list = []
    for row in readCSV:
        packages_data_list.append(row)
    return packages_data_list


data_list = get_data_from_csv("Distance.csv")

for item in data_list:
    print(item)


