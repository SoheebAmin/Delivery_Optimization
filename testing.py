# This file contains functions written for testing and verification purposes.

# TESTING DISTANCE_TO_NEXT_ADDRESS():
# with_zip = distance_matrix[0][3]  # sample starting address. Has a zip attached
# a = CSV_Import.remove_zip(with_zip)  # I have to remove zip to make comparison
# package = hashtable.search(3)  # sample random package
# b = package.address  # sample destination from said package
# distance_to_next_address(a, b)


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
