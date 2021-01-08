# Soheeb Amin's Delivery Optimization project. Student ID 001452292.

import datetime
import CSV_Import
import Hashtable
import Package

# call the function to read the rows of the packages csv into a 2D array
packages_matrix = CSV_Import.get_data_from_csv("Packages.csv")

# call the same function for the distance table
distance_matrix = CSV_Import.get_data_from_csv("Distance.csv")

# initialize the hashtable
hashtable = Hashtable.HashTable(60)

# start the day
current_time = datetime.time(8, 00, 00)


# time objects don't allow you to add minutes, so this function was copied over from Stackoverflow question 59465525.
def add_minutes(tm, minutes1):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(minutes=minutes1)
    return fulldate.time()


# function to place each row of the matrix into a package object, which is then hashed into the hash table
def create_and_hash_package_objects(matrix):
    packages_list = []
    for inner_list in matrix:
        package = Package.Package(
            inner_list[0],  # ID
            inner_list[1],  # Address
            inner_list[2],  # City
            inner_list[3],  # State
            inner_list[4],  # Zip
            inner_list[5],  # Deadline
            inner_list[6],  # Mass
            inner_list[7],  # Note
            None)  # time delivered
        hashtable.insert(package)


create_and_hash_package_objects(packages_matrix)

truck_1 = [1, 13, 14, 15, 19, 16, 20, 29, 31, 34, 37, 40]  # Early deadline packages and go-together packages.
truck_2 = [3, 6, 9, 18, 25, 28, 32, 36, 38, 30, 33, 35, 39]  # delayed till 9:05 packages + misc conditions.
truck_3 = [2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, ]  # the rest, but last 4 added to truck 2.

