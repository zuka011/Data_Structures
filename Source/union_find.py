

from typing import Iterable, Iterator


class UnionFind:
    """This is a union find data structure."""

    def __init__(self, size: int=0, data: Iterable=None):   
        """Constructor for the union find structure.

        This structure creates a bijection between it's elements and 
        numbers (initial groups) in the range [1, #elements in union find].
        Later these indices can be used to operate the union find structure.

        example:
            u_find = UnionFind(["cat", "dog", 1, (2, 3)])

        This will associate the passed values with the numbers [1, 2, 3, 4]

        Optional parameters:
            
        size - if specified, will create a union find structure of size {size}

        data - if specified, will create a union find structure from the elements in {data}.
        {data} must be an iterable object.

        if both are specified and {size} is less than #elements in {data}, it will be ignored,
        otherwise the remaining indices will be filled with None values. 
        O(N), N = #elements in union find"""

        if data is None:
            self.__list = [None] + [[None, i] for i in range(1, size+1)]
        elif hasattr(data, "__iter__"):              
            self.__list = [None] + [[data[i], i+1] for i in range(len(data))] + [[None, len(data)+1+i] for i in range(size - len(data))]
        else:
            raise TypeError("Passed data is not an iterable.")

        self.__groups = len(self.__list) - 1

    def __len__(self) -> int:
        """Returns the number of groups in the union find structure. O(1)"""

        return self.__groups

    def __str__(self) -> str:
        """Returns a string representation of the union find
        in the form (element, group number). The group number
        may be any number, but will be the same for elements
        that belong to the same group. O(N), N = #elements in union find"""

        return str([tuple(pair) for pair in self.__list[1:]])

    def __iter__(self) -> Iterator:
        """Returns an iterator to pairs of data in the form
        (element, group number), for all elements in the 
        union find. O(N), N = #elements in union find"""

        return iter([tuple(pair) for pair in self.__list[1:]])

    def add_element(self, element)  -> None:
        """Adds an element to the union find structure. O(1)"""

        self.__list.append([element, len(self.__list)])
        self.__groups += 1

    def set_element(self, index: int, element) -> None:
        """Associates the number {index} with {element}. O(1)"""

        if index < 1 or index > len(self.__list):
            raise IndexError("No such index in union find.")

        if index == len(self.__list):
            self.add_element(element)
        else:
            self.__list[index][0] = element

    def is_same_group(self, index_1: int, index_2: int) -> bool:
        """Returns True if element at {index_1} is in the same 
        group as the element at {index_2}. (Amortized) O(1)"""

        self.__check_bounds(index_1)
        self.__check_bounds(index_2)
        
        root_1 = self.__find_root(index_1)
        root_2 = self.__find_root(index_2)

        return root_1 == root_2

    def merge(self, index_1: int, index_2: int) -> None:
        """Merges the groups of the element at {index_1} and the 
        element at {index_2}. (Amortized) O(1)"""

        root_1 = self.__find_root(index_1)
        root_2 = self.__find_root(index_2)

        if root_1 != root_2:
            self.__groups -= 1

        if root_1 < root_2:
            self.__list[root_2][1] = root_1
        else:
            self.__list[root_1][1] = root_2

    def __check_bounds(self, index: int):
        """Checks to see if {index} is within the union
        find structures bounds e.i. in the range [1, #elements in the union find]."""

        if index < 1 or index >= len(self.__list):
            raise IndexError("No such index in union find.")

    def __find_root(self, index: int):
        """Finds and returns the index of the root for the
        group which element at {index} belongs to. This method
        implements path compression for the union find structure."""

        passed_indices = []

        while self.__list[index][1] != index:
            passed_indices.append(index)
            index = self.__list[index][1]

        for passed_index in passed_indices:
            self.__list[passed_index][1] = index

        return index



