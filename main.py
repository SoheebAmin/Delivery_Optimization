# Soheeb Amin's Delivery Optimization project. Student ID 001452292.

import datetime
import CSV_Import
import Hashtable
import Package

# call the function to read the rows of the packages csv into a 2D array
packages_matrix = CSV_Import.get_data_from_csv("Packages.csv")

# call the same function for the distance table, using the optional parameter to strip the zip codes
distance_matrix = CSV_Import.get_data_from_csv("Distance.csv")

# initialize the hashtable
hashtable = Hashtable.HashTable(60)

# start the day
current_time = datetime.time(8, 00, 00)


def minutes_passed(miles_to_travel):
    """
    :param miles_to_travel
    :return: The minutes it will take to travel given miles
    Complexity: O(1)

    This function takes in the miles a truck needs to travel to its next destination, and returns the number of minutes
    the travel will take.
    """
    truck_speed = 18  # the given MPH of the truck.
    minutes = (miles_to_travel / truck_speed) * 60
    return minutes


def add_minutes(current_time_object, minutes_to_add):
    """
    :param current_time_object: the global time object holding the current time
    :param minutes_to_add: the minutes we have already determined should be added to the time.
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
    :param matrix: The packages matrix pulled from the CSV
    :return: None. The already initialized hashtable will be filled.
    Complexity: O(n)

    This function places each row of the provided matrix into a package object, which is then hashed into the hash table
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


def distance_to_next_address(current_package_location, destination):
    """
    :return: the distance in miles to the next address
    """
    print(f"starting at {current_package_location}, ending at {destination}")  # shows starting and ending address
    current_address_row = []  # initialize variable for row check
    for row in distance_matrix:  # iterate over rows in distance table
        start = CSV_Import.remove_zip(row[0])  # gets first index which is address, strip the zip code.
        if start == current_package_location:  # if the address matches current location, distance in this row
            current_address_row = row  # sets this row as the one to check and breaks
            break
    destination_address_row = distance_matrix[0]  # the matching destination is found in the matrix's first index
    index = 0  # variable to count which index we need to get the distances in the current address row
    for address in destination_address_row:  # iterate over the destination row
        end = CSV_Import.remove_zip(address)  # removes the zip for the address to check
        if end == destination:  # if we found the address, break, since we found the correct index
            break
        else:  # if not, then update to next index, which will be checked next iteration
            index += 1
    if not current_address_row:
        print("blank!")
        return -1
    distance = current_address_row[index]
    print(distance)
    distance_as_float = float(distance)
    return distance_as_float


def determine_shortest_address(current_address, truck):
    """
    :param current_address: The address that the truck is currently at.
    :param truck: the list which abstracts the truck and the current packages it holds.
    :return: the best address to go to for delivery
    Complexity: TODO!!!!!!!!!

    This function takes the current addres of the truck, examines its current contents, and determines the next best
    location to travel to based on the nearest neighbor algorithm.
    """
    next_address = ""
    shortest_distance = 999
    for package_id in truck:
        package = hashtable.search(package_id)
        if package.address != current_address:  # ignores any package that has the same address as the current one.
            distance = distance_to_next_address(current_address, package.address)
            if distance < shortest_distance:
                next_address = package.address
                shortest_distance = distance
    return next_address


truck_1 = [1, 13, 14, 15, 19, 16, 20, 29, 31, 34, 37, 40]  # Early deadline packages and go-together packages.
truck_2 = [3, 6, 9, 18, 25, 28, 32, 36, 38, 30, 33, 35, 39]  # delayed till 9:05 packages + misc conditions.
truck_3 = [2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]  # the rest, but last 4 added to truck 2.

print(f"shortest: {determine_shortest_address('HUB', truck_1)}")


# TESTING DISTANCE_TO_NEXT_ADDRESS():
# with_zip = distance_matrix[0][3]  # sample starting address. Has a zip attached
# a = CSV_Import.remove_zip(with_zip)  # I have to remove zip to make comparison
# package = hashtable.search(3)  # sample random package
# b = package.address  # sample destination from said package
# distance_to_next_address(a, b)


# for row in distance_matrix:
#     print(row)
#
#
# def confirm_address_in_hashtable():
#     for i in range(1, 41):
#         package = hashtable.search(i)
#         address_to_check = package.address
#         found = False
#         for item in distance_matrix[0]:
#             item = CSV_Import.remove_zip(item)
#             if address_to_check == item:
#                 print(f"For id {i}, address {item} is confirmed!")
#                 found = True
#         if not found:
#             print(f"{i} not found for address {address_to_check}")
#
#
# confirm_address_in_hashtable()
