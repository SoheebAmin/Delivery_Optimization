# This hash table is based om ChainingHashTable one provided in the ZyBooks' textbook from Chapter 7.8.
# The hash function was self developed, and the buckets are lists which contain lists which act as k/v pair for chaining

class HashTable:
    def __init__(self, buckets):  # provide number of buckets
        self.table = []  # empty table
        for i in range(buckets):  # create empty buckets with provided size
            self.table.append([])

    def insert(self, package):
        """
        :param package:
        :return:
        Time Complexity:
        Space Complexity:

        This methods gets the bucket list where this item will go, using its ID as a key
        """
        bucket = (package.id ** 2 * 50331653) % len(self.table)  # hash function: square and multiply by a large prime.
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        key_value_pair = [package.id, package]
        bucket_list.append(key_value_pair)

    def lookup(self, key):
        """
        :param key: package ID
        :return: The package if found, None if not found
        Time Complexity:
        Space Complexity:

        This method searches the first index of every item in the hashtable to see if it is the key of the hashed item.
        """
        # get the bucket list where this key would be.
        bucket = (key ** 2 * 50331653) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list by iterating over every key-value pair and checking the keys.
        if bucket_list:
            for hashed_item in bucket_list:
                if hashed_item[0] == key:
                    return hashed_item[1]
        else:
            # the key is not found.
            return None

    def remove(self, key):
        """
        :param key:
        :return:
        Time Complexity:
        Space Complexity:

        This method removes an item with matching key from the hash table.
        """
        # get the bucket list where this item will be removed from.
        bucket = (key ** 2 * 50331653) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list by iterating over every key-value pair and checking the keys.
        if bucket_list:
            for hashed_item in bucket_list:
                if hashed_item[0] == key:
                    return bucket_list.remove(hashed_item)

    def display(self):
        """
        Time Complexity:
        Space Complexity:
        :return:
        """
        for item in self.table:
            print(item)
