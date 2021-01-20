## Delivery Optimization With self-build Hash Table

This program runs a delivery algorithm by pulling data from two CSV files: packages.csv, which contains details about 40 different pacakges (including special delivery 
conditions), and a distance table to provide the distance from one location to another.

The program creates package objects and insets them to a chaining hash table. The objects then run via a self-written greedy algorithm following the nearest neighbor approach.
Packages are also modified to include their delivery time to ensure a timely delivery, and are then re-inserted into the hash table.

The program includes verification functions for all deliveries as well as specific delivery times.

# Output of 40 deliveries
