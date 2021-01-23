

class UnionFind:
    """This is a union find data structure."""

    def __init__(self, size=None, data=None):   
        """Constructor for the union find structure.

        This structure creates a bijection between it's elements and
        numbers in the range [1, #elements in union find].

        example:
            u_find = UnionFind(["cat", "dog", 1, (2, 3)])

        This will associate the passed values with the numbers [1, 2, 3, 4]

        Optional parameters:
            
        size - if specified, will create a union find structure of size {size}

        data - if specified, will create a union find structure from the elements in {data}

        if both are specified and {size} is less than #elements in data, it will be ignored,
        otherwise the remaining indices will be filled with None values. 
        O(N), N = #elements in union find"""

        raise NotImplementedError

    def __len__(self):
        """Returns the size of the union find structure. O(1)"""

        raise NotImplementedError

    def __str__(self):
        """Returns a string representation of the union find
        in the form (element, group number). The group number
        may be any number. O(N), N = #elements in union find"""

        raise NotImplementedError

    def __iter__(self):
        """Returns an iterator to pairs of data in the form
        (element, group number), for all elements in the 
        union find. O(N), N = #elements in union find"""

        raise NotImplementedError

    def add_element(self, element):
        """Adds an element to the union find structure. O(1)"""

        raise NotImplementedError

    def set_element(self, index, element):
        """Associates the number {index} with {element}. O(1)"""

        raise NotImplementedError

    def same_group(self, index_1, index_2):
        """Returns True if element at {index_1} is in the same 
        group as the element at {index_2}. (Amortized) O(1)"""

        raise NotImplementedError

    def merge(self, index_1, index_2):
        """Merges the groups of the element at {index_1} and the 
        element at {index_2}. (Amortized) O(1)"""

        raise NotImplementedError

