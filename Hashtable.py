# This hash table is a modified version of ChainingHashTable one provided in the ZyBooks' textbook from Chapter 7.8.

# method to add / lookup / delete all go here.

class HashTable:

    def __init__(self, buckets):

        self.table = []
        for i in range(buckets):
            self.table.append([])

    # Inserts packages into the hash table.
    def insert(self, package):
        # get the bucket list where this item will go, using its ID as a key
        bucket = hash(package.id) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        key_value_pair = [package.id, package]
        bucket_list.append(key_value_pair)

    # Searches the first index of every item in the hashtable to see if it is the key of the hashed item.
    # If so,returns the item. If not, returns None
    def lookup(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list by iterating over every key-value pair and checking the keys.
        if bucket_list:
            for hashed_item in bucket_list:
                if hashed_item[0] == key:
                    return hashed_item[1]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table. WRONG!
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list by iterating over every key-value pair and checking the keys.
        if bucket_list:
            for hashed_item in bucket_list:
                if hashed_item[0] == key:
                    return bucket_list.remove(hashed_item)

    def display(self):
        for item in self.table:
            print(item)


