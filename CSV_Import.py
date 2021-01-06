# import from CSV to data structures.
import csv
import io

def get_packages_data_from_CSV(packages_CSV):
    """"This function goes through the given CSV files and saves packages together in an a 2D array
    Runtime: """

    csvfile = io.open(packages_CSV, mode='r', encoding='utf-8-sig')  # utf-8 spec required to remove chars at start
    readCSV = csv.reader(csvfile, delimiter=",")
    packages_data_list = []
    for row in readCSV:
        packages_data_list.append(row)
    return  packages_data_list


def get_distance_data_from_CSV():
    """"This function goes through the given CSV files and saves packages together in an a 2D array
    Runtime: """


data_list = get_packages_data_from_CSV("Packages.csv")
print(data_list)


