# -*-coding:utf-8 -*-
"""Hash Table Algorithim Implementation."""


class HashTable(object):
    """Defining hash table class."""

    def __init__(self, table_size):
        """Inititalize hash table instance."""
        try:
            int(table_size)
            self.table = [None] * table_size
        except TypeError:
            print("You must enter an integer value.")

    def set(self, key, value):
        """Store a given value of a given key into hashtable."""
        if type(key) == str:
            index_spot = self._hash(key)
            hit = self._to_search(key, index_spot)
            if hit is None:
                self.table[index_spot] = [(key, value)]
            elif hit is False:
                self.table[index_spot].append((key, value))
            else:
                self.table[index_spot][hit[0]] = (key, value)
        else:
            raise TypeError("Key must be a string.")

    def _hash(self, key):
        """Hash the key provided."""
        hash_num = 0
        for letter in key:
            hash_num += ord(letter)
        return hash_num % len(self.table)

    def _to_search(self, key, index_spot):
        """Return a key if found, else return None."""
        if self.table[index_spot] is not None:
            for index, value in enumerate(self.table[index_spot]):
                if value[0] == key:
                    return (index, value)
            return False
        else:
            return None

    def get(self, key):
        """Return the value stored with the given key."""
        index_spot = self._hash(key)
        if type(index_spot) == tuple:
            value = self._to_search(key, index_spot)[1]
            return value
        else:
            raise KeyError("Key is not in dictionary!")

if __name__ == '__main__':
    h = HashTable(1)
    h.set("keyone", 1)
    h.set("keytwo", 3)
    h.set("keytwo", 7)
    print(h.table)
