# This hash table is a modified version of ChainingHashTable one provided in the ZyBooks' textbook from Chapter 7.8.

# method to add / lookup / delete all go here.

class HashTable:

    def __init__(self, buckets):

        self.table = []
        for i in range(buckets):
            self.table.append([])
        print(self.table)

    # Inserts a new item into the hash table.
    def insert(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)



