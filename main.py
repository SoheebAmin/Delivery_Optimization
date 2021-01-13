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
hashtable = Hashtable.HashTable(100)

# A variable to be set by the user for if step-by-step print statements should be visible.
show_status = True


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
    # print(f"starting at {current_package_location}, ending at {destination}")  # shows starting and ending address
    current_address_row = []  # initialize variable for row check
    for row in distance_matrix:  # iterate over rows in distance table
        start = CSV_Import.remove_zip(row[0])  # gets first index which is address, strip the zip code.
        if start == current_package_location:  # if the address matches current location, distance in this row
            current_address_row = row  # sets this row as the one to check and breaks
            break
    if not current_address_row:  # a check ensure an address match was found.
        print("no row matched!")
        return -1
    destination_address_row = distance_matrix[0]  # the matching destination is found in the matrix's first index
    index = 0  # variable to count which index we need to get the distances in the current address row
    for address in destination_address_row:  # iterate over the destination row
        end = CSV_Import.remove_zip(address)  # removes the zip for the address to check
        if end == destination:  # if we found the address, break, since we found the correct index
            break
        else:  # if not, then update to next index, which will be checked next iteration
            index += 1
    distance = current_address_row[index]
    distance_as_float = float(distance)
    return distance_as_float


def determine_shortest_address(current_address, truck):
    """
    :param current_address: The address that the truck is currently at.
    :param truck: the list which abstracts the truck and the current packages it holds.
    :return: the best address to go to for delivery
    Complexity: TODO!!!!!!!!!

    This function takes the current address of the truck, examines its current contents, and determines the next best
    location to travel to based on the nearest neighbor algorithm.
    """
    next_address = ""  # initialize next address
    shortest_distance = float("inf")  # initialize the shortest distance, default at infinity before comparisons made.
    for package_id in truck:  # iterate over the IDs in the truck
        package = hashtable.lookup(package_id)  # use the hashtable to grab the correct package
        if package.address != current_address:  # ignores any package that has the same address as the current one.
            distance = distance_to_next_address(current_address, package.address)  # calls func. for dist. for each
            if distance < shortest_distance:  # if the distance of this package is less than the current lowest...
                next_address = package.address  # mark it as the next address to go to
                shortest_distance = distance  # and update the shortest distance variable
    return [next_address, shortest_distance]  # return the address to go to next, and the distance that it would take.


truck_1 = [1, [1, 13, 14, 15, 19, 16, 20, 29, 31, 34, 37, 40]] # Early deadline packages and go-together packages.
truck_2 = [2, [3, 6, 18, 25, 26, 27, 28, 32, 36, 38, 30, 33, 35, 39]]  # delayed till 9:05, wrong address, only truck 2
truck_3 = [3, [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24]]  # the rest, but last 6 added to truck 2.

def update_address(address_to_update, package):
    package


def execute_truck_delivery(truck_with_number, departing_time, status_statements):
    """
    :param status_statements: a boolean which either turns the status statements on or off.
    :param departing_time: The time the truck will leave to start deliveries
    :param truck: The truck which needs to run deliveries
    :return: The time after the deliveries have completed.
    Complexity: TODO!!!!!!!!!

    This function...
    """
    truck = truck_with_number[1]
    if status_statements:
        truck_number = truck[0]
        print(f"\nSTARTING DELIVERY FOR TRUCK {truck_number}: {len(truck)} packages\n")
    current_time = departing_time  # marks the starting time as the time the truck is set to depart
    next_location_info = determine_shortest_address('HUB', truck)  # call func to get nearest address + dist from hub
    delivery_location = next_location_info[0]  # store nearest address in variable
    total_miles_travelled = next_location_info[1]  # add distance to our distance counter
    minutes_to_add = minutes_passed(total_miles_travelled)  # using the distance travelled, get how many minutes passed
    if status_statements:
        print(f"Departing from Hub. Nearest neighbour: {delivery_location}, which is {total_miles_travelled} away")
    current_time = add_minutes(current_time, minutes_to_add)  # move clock up by the calculated minutes that passed
    while truck:  # while the truck has not been emptied
        unload_for_delivery = []  # list to hold all packages in the same location
        for package_id in truck:  # iterate over IDs in truck
            package = hashtable.lookup(package_id)  # pulls actual objects from the hashtable
            if package.address == delivery_location:  # if the address on the package matches our delivery location...
                unload_for_delivery.append(package)  # then we add them to the list of packages we unload for deliver
        for package in unload_for_delivery:  # iterate over packages to be delivered
            # if status_statements:
            # print(f"state of truck{truck}, package to deliver: {package.id}")
            hashtable.remove(package.id)  # remove the old version of the package from the hashtable
            package.delivery_time = current_time  # add the delivery time to the package
            hashtable.insert(package)  # insert the delivered package back into the hash table
            if status_statements:
                print(f"package with ID {package.id} delivered at {current_time}.")
            truck.remove(package.id)  # check off the packages that were just delivered
        if status_statements:
            print(f"Delivery to {delivery_location} complete. {len(truck)} packages left: {truck}\n")
        if truck:  # if not empty, updates delivery and distance info for next run of iteration
            next_location_info = determine_shortest_address(delivery_location, truck)
            delivery_location = next_location_info[0]
            miles_to_travel = next_location_info[1]
            total_miles_travelled += miles_to_travel
            minutes_to_add = minutes_passed(miles_to_travel)  # get the time it takes to go the next location
            current_time = add_minutes(current_time, minutes_to_add)  # and add it to the current time
            if status_statements:
                print(f"Next nearest neighbour: {delivery_location}, which is {miles_to_travel} away")
        else:  # if it is empty...
            miles_to_hub = distance_to_next_address(delivery_location, 'HUB')  # gets the miles to the hub
            total_miles_travelled += miles_to_hub  # adds the miles to the total
            minutes_to_add = minutes_passed(miles_to_hub)  # get the time it takes to get back to the hub
            current_time = add_minutes(current_time, minutes_to_add)  # and add it to the final time.
            if status_statements:
                print(f"Returned to hub from {delivery_location}, in {miles_to_hub} miles, total {total_miles_travelled}")
                print(f"Arrival Time: {current_time}\n")
    return [current_time, total_miles_travelled]


def verify_delivery_on_time():
    """
    :return:
    Comlexity: O(n^2)

    This function will iterate over the hash table after deliveries, and check delivery time objects against the
    required times of delivery (which are converted from strings to time objects) to ensure all deliveries are on time.
    """
    delivery_success = True  # assumes true, but will change to false if delivery error detected
    failure_list = []  # a list to hold the ID of failed packages, if any.
    delivery_count = 0  # variable to count how many packages have a delivery time.
    for bucket in hashtable.table:  # iterate over buckets
        if bucket:  # ignore empty buckets
            for kv_pair in bucket:  # for each key/value pair in the bucket...
                package = kv_pair[1]  # grab the package object
                p_id = package.id   # note the ID
                time_delivered = package.delivery_time  # store the recoded time of delivery
                if time_delivered:  # if the package was delivered (which all should be)
                    delivery_count += 1  # add the counter (which should total 40 by the end)
                required_time_raw = package.deadline  # grab the string which contains the deadline from the package.
                if required_time_raw != 'EOD':  # for 'EOD', there is no deadline so are on time as long as delivered.
                    as_list = required_time_raw.split()  # split the string which contains the time into a list
                    time_alone = as_list[0]  # grab the time itself.
                    required_time = datetime.datetime.strptime(time_alone, '%H:%M').time()  # convert it to time object.
                    if required_time < time_delivered:  # if the delivery is later than the required time:
                        print(f"package with id {p_id} delivered at {time_delivered}, but deadline was {required_time}")
                        failure_list.append(package.id)  # add it to the failure list.
                        delivery_success = False  # set success to false
    if delivery_success:  # if success still remains true after that loop...
        print(f"{delivery_count} packages were delivered, and all met their deadlines.")
    else: # if not, print failures and return false.
        print(f"{len(failure_list)} packages failed to be on time: {failure_list}")
    return delivery_success


# Set the departure time for the first two trucks
depart_time_for_truck_1 = datetime.time(8, 00, 00)
depart_time_for_truck_2 = datetime.time(9, 0o5, 00)

# Execute deliveries for truck 1, and saves the the time after deliveries, and the total miles travelled.
time_and_distance_after_truck_1 = execute_truck_delivery(truck_1, depart_time_for_truck_1, show_status)

# Sets truck 3's departure time based on truck 1's arrival time (driver of truck 1 takes over truck 3)
depart_time_for_truck_3 = add_minutes(time_and_distance_after_truck_1[0], 60)

# Execute deliveries for truck 2, and saves the information about its time and distance:
time_and_distance_after_truck_2 = execute_truck_delivery(truck_2, depart_time_for_truck_1, show_status)

# Execute deliveries for truck 3, starting at the time truck 1 arrives + 1 hour to allow for package time correction
time_and_distance_after_truck_3 = execute_truck_delivery(truck_3, depart_time_for_truck_3, show_status)

# The total miles for each truck as found in the second item in the returned list after delivery.
truck_1_miles = time_and_distance_after_truck_1[1]
truck_2_miles = time_and_distance_after_truck_2[1]
truck_3_miles = time_and_distance_after_truck_3[1]

# Total miles by the end of deliveries, as optimized by the nearest neighbor algorithm
combine_miles = truck_1_miles + truck_2_miles + truck_3_miles
print(f"\nThe total miles travelled by all three trucks: {combine_miles}")


verify_delivery_on_time()

#     if bucket:
#         for kv_pair in bucket:
#             id = kv_pair[1].id
#             time_delivered = kv_pair[1].delivery_time
#             print(f"package with id {id} was delivered at {time_delivered}")


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
