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


def add_minutes(current_time_object, minutes_to_add):
    """
    :param current_time_object:
    :param minutes_to_add:
    :return: current_time_object with minutes updated by minutes_to_add
    Complexity: O(1)

    Time objects does not have an add time method, so this function was modified from question 59465525 on
    Stackoverflow to take a time object and add a set amount of minutes to it.

    """
    full_date = datetime.datetime(100, 1, 1, current_time_object.hour, current_time_object.minute,
                                  current_time_object.second)
    full_date = full_date + datetime.timedelta(minutes=minutes_to_add)
    return full_date.time()


def create_and_hash_package_objects(matrix):
    """
    :param matrix: 
    :return: None
    Complexity: O(n)

    This function places each row of the provode matrix into a package object, which is then hashed into the hash table
    """

    for inner_list in matrix:
        package = Package.Package(
            int(inner_list[0]),  # ID, converted to Int
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


def address_lookup(where_truck_is, where_truck_goes):
    pass


truck_1 = [1, 13, 14, 15, 19, 16, 20, 29, 31, 34, 37, 40]  # Early deadline packages and go-together packages.
truck_2 = [3, 6, 9, 18, 25, 28, 32, 36, 38, 30, 33, 35, 39]  # delayed till 9:05 packages + misc conditions.
truck_3 = [2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]  # the rest, but last 4 added to truck 2.



confirm_address_in_hashtable()