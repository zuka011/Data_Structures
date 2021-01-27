import sys

sys.path.append(r"..")

from Source.doubly_linked_list import DoublyLinkedList


from typing import Callable, Iterable

class HashTable:
    """This is a Hash Table data structure.

    This implementation uses separate chaining to resolve collisions."""

    __INIT_N_BUCKETS = 10

    def __init__(self, hash_function: Callable=hash, key: Callable=lambda x: x, data: Iterable=None):
        """Constructor for Hash Table.

        The user can supply a hash function {hash_function} which the
        Hash Table will use to store elements. If a hash function is 
        not supplied, hash() will be used to get the appropriate hash
        value. 
        
        The == operator is used to determine if two elements are equal. 

        (optional) {data} will be added to the hash table. {data} must
        be an iterable object. O(N), N = #elements in data*
        
        * - Time complexity estimates are given assuming the supplied
        hash function is relatively uniform."""

        if not hasattr(hash_function, "__call__"):
            raise ValueError("{hash_function} must be a callable object.")

        if not hasattr(key, "__call__"):
            raise ValueError("{key} must be a callable object.")

        self.__hash_function = self.__hash_function_decorator(hash_function, key)

        self.__buckets = [None] * HashTable.__INIT_N_BUCKETS
        self.__n_buckets = HashTable.__INIT_N_BUCKETS
        self.__size = 0
        
        if hasattr(data, "__iter__"):
            for element in data:
                self.add(element)
        elif data is not None:
            raise ValueError("{data} must be an iterable object.")

    def __len__(self):
        """Returns the number of elements in the structure. O(1)"""
        
        return self.__size

    def __str__(self):
        """Returns a string representation of all elements in the
        structure. O(N), N = #elements in the Hash Table"""

        return str([element for element in self])

    def __iter__(self):
        """Returns an iterator over all the elements in the structure.
        O(N), N = #elements in the Hash Table"""

        elements = []
        for bucket in self.__buckets:
            if bucket is not None:
                elements += [elem for elem in bucket]

        return iter(elements)

    def add(self, element) -> bool:
        """Adds an element to the Hash Table if it doesn't already 
        exist. Returns true if the element was not already present. O(1)"""

        if self.__size == self.__n_buckets:
            self.__resize()

        if self.contains(element):
            return False

        hash_value = self.__hash_function(element) % self.__n_buckets

        if self.__buckets[hash_value] is None:
            self.__buckets[hash_value] = DoublyLinkedList()

        self.__buckets[hash_value].push_back(element)
        self.__size += 1
        
        return True

    def remove(self, element) -> bool:
        """Removes an element from the Hash Table if it exists. Returns
        true if the element was present. O(1)"""

        if not self.contains(element):
            return False

        hash_value = self.__hash_function(element) % self.__n_buckets

        self.__buckets[hash_value].remove(element)
        self.__size -= 1
        
        return True

    def contains(self, element) -> bool:
        """Returns true if the element is present in the Hash Table. O(1)"""

        hash_value = self.__hash_function(element) % self.__n_buckets

        if self.__buckets[hash_value] is None:
            return False
        else:
            return self.__buckets[hash_value].contains(element)

    def map(self, map_function: Callable, *map_arguments) -> None:
        """Iterates over all elements in the Hash Table and passes 
        it to {map_function} along with {*map_arguments}. 
        O(N), N = #elements in the Hash Table"""

        for element in self:
            map_function(element, *map_arguments)

    def __resize(self):
        """Creates a new list twice the size of the previous one.
        Rehashes every element in the previous list and transfers
        them to the new one."""

        self.__n_buckets *= 2

        new_buckets = [None] * self.__n_buckets
        old_elements = iter(self)

        self.__buckets = new_buckets
        self.__size = 0

        for element in old_elements:
            self.add(element)

    def __hash_function_decorator(self, hash_function, key_function):
        """Returns a function that uses {key_function} on the passed value,
        before passing it to {hash_function}."""

        def wrapper(element):
            return hash_function(key_function(element))
            
        return wrapper
