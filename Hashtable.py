# This hash table is based om ChainingHashTable one provided in the ZyBooks' textbook from Chapter 7.8.
# The hash function was self developed, and the buckets are lists which contain lists which act as k/v pair for chaining

class HashTable:
    """
    This is the creation of the hash table class, which uses lists within list, as well as a hash function, to insert
    and look up data in constant time. The inner lists always contain two items, the first being the key, and the second
    being the value associated with the key. If there is a collision, the lists are chained together, making this a
    chaining hash table.
    """
    def __init__(self, buckets):
        """
        :param buckets: The number of buckets to initiate the hash table with.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.table = []  # empty table
        for i in range(buckets):  # create empty buckets with provided size
            self.table.append([])  # add the buckets to the table

    def insert(self, package):
        """
        :param package: The package to insert into the hash table.
        :return: None.
        Time Complexity: O(1)
        Space Complexity: O(1)

        This methods gets the bucket list where this item will go, using its ID as a key. The hash function uses the
        ID and a large prime number, modulo the length of the table, to choose a bucket for it.
        """
        bucket = (package.id ** 2 * 50331653) % len(self.table)  # hash function: square and multiply by a large prime
        bucket_list = self.table[bucket]  # the number given is the bucket to insert to
        key_value_pair = [package.id, package]  # set the key/value pair as the package ID and the package itself
        bucket_list.append(key_value_pair)  # insert it into the bucket number given by the hash function

    def lookup(self, key):
        """
        :param key: package ID
        :return: The package if found, None if not found
        Time Complexity: O(1)
        Space Complexity: O(1)

        This method searches the first index of every item in the hashtable to see if it is the key of the hashed item.
        """
        bucket = (key ** 2 * 50331653) % len(self.table)  # get the bucket by using hash function
        bucket_list = self.table[bucket]  # grab the list where the value for that key would be
        if bucket_list:  # only iterate if the bucket list isn't empty
            for hashed_item in bucket_list:  # look through the bucket
                if hashed_item[0] == key:  # if the first item is the key
                    return hashed_item[1]  # return the second item, which will be the value
        else:
            return None # the key is not found.

    def remove(self, key):
        """
        :param key: The key for the value to remove from the hash table
        :return: None.
        Time Complexity: O(1)
        Space Complexity: O(1)

        This method removes an item with matching key from the hash table.
        """
        bucket = (key ** 2 * 50331653) % len(self.table)  # get the bucket by using hash function
        bucket_list = self.table[bucket]  # grab the list where the value for that key would be
        for hashed_item in bucket_list:  # for the items in that list...
            if hashed_item[0] == key:  # if that item is the key...
                bucket_list.remove(hashed_item)  # then remove that item

