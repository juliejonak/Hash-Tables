

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for i in string:
        hash = (hash * 33) + ord(i)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    linked_pair = LinkedPair(key, value)
    stored_linked_pair = hash_table.storage[index]

    if hash_table.storage[index] is not None:
        if linked_pair.key != stored_linked_pair.key:
            # What do we do? Create a new index to prevent overwriting?
            # Expand the capacity to change index?
            print(f"Warning: Index at {str(index)} is currently {hash_table.storage[index]}.")

    else:
        hash_table.storage[index] = linked_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key != key:
            print(f'Unable to remove item with key: {key}')
    else:
        # Need to change the self.next to the node pointing to this one?
        removed_next = hash_table.storage[index].next
        hash_table.storage[index] = None
        # How do we find the index that pointed to this one?


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))
    
    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value
        print(f'Key {key} at that index does not match.')
    
    print(f'Unable to find value with key: {key}')
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2
    new_storage = [None] * new_capacity

    for i in range(hash_table.storage):
        new_storage[i] = hash_table.storage[i]
    
    hash_table.storage = new_storage
    hash_table.capacity = new_capacity


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
