# -*-coding:utf-8 -*-
"""Hash table algorythim implementation."""


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
            hash_num = 0
            for letter in key:
                hash_num += ord(letter)
            index_spot = hash_num % len(self.table)
            hit = self._to_search(key, value, index_spot)
            if hit is None:
                self.table[index_spot] = [(key, value)]
            elif hit is False:
                self.table[index_spot].append((key, value))
            else:
                self.table[index_spot][hit[0]] = (key, value)
        else:
            raise TypeError("Key must be a string.")

    def _to_search(self, key, index_spot):
        """Return a key if found, else return None."""
        if self.table[index_spot] is not None:
            for index, value in enumerate(self.table[index_spot]):
                if value[0] == key:
                    return (index, value)
            return False
        else:
            return None
