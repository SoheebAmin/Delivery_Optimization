# Soheeb Amin's Delivery Optimization project. Student ID 001452292.

import CSV_Import
import Hashtable
import Package

# call the function to read the rows of the packages csv into a 2D array
packages_matrix = CSV_Import.get_data_from_csv("Packages.csv")

# call the same function for the distance table
distance_matrix = CSV_Import.get_data_from_csv("Distance.csv")


# function to place each row of the matrix into a package object.
# Once you have hash table, after creating each obj, call hash func to place it in table. Key = ID. Val = Obj itself
def create_package_objects(matrix):
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
            None)           # time delivered
        packages_list.append(package)
    return packages_list


package_obj_in_list = create_package_objects(packages_matrix)

truck_1 = [1, 13, 14, 15, 19, 16, 20, 29, 31, 34, 37, 40]  # Early deadline packages and go-together packages.
truck_2 = [3, 6, 9, 18, 25, 28, 32, 36, 38, 30, 33, 35, 39]  # delayed till 9:05 packages + misc conditions.
truck_3 = [2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, ]  # the rest, but last 4 added to truck 2.

hash_t = Hashtable.HashTable(10_000_000_000)
