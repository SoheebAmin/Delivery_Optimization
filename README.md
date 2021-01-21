# Delivery Optimization with Self-Built Hash Table

This program runs a delivery algorithm by pulling data from two CSV files: packages.csv, which contains details about 40 different packages (including special delivery 
conditions), and a distance table to provide the distance from one location to another.

The program creates package objects and insets them to a chaining hash table. The objects then run via a self-written greedy algorithm following the nearest neighbor approach.
Packages are also modified to include their delivery time to ensure a timely delivery, and are then re-inserted into the hash table.

The program includes verification functions for all deliveries as well as specific delivery times.

## Delivery Algorithm Running

![Algorithm Running](Screenshots/NN_Running.png?raw=true "Algorithm Running")

The print statements make every delivery clear as the algorithm runs, providing updates on where the truck is, what packages it is delivering, and what the nearest neighbor algortithm is determining as the closest location to travel to next.


## Output of 40 deliveries

![40 Delivery Output](Screenshots/Miles_and_Deadline_Verification.png?raw=true "Delivery Output")

The 40 packages objects all have their delivery times appended to them as a field. This delivery time is then compared to the the the stated deadline field (with some data and type manipulation) and then the results are shown to confirm all deliveries were on time.


## Custom Time Verification (10am example)

![Custom Time Verification](Screenshots/All_packages_10am.png?raw=true "10am Verification")

The user can input any time that day, and be given the delivery status of every package at that time of day.
