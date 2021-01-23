from functools import singledispatch, total_ordering

@total_ordering
class _Infinity:
    """This is a class to represent infinity. 

    if an instance of this class is x then:
        
    if it's sign is negative:
        x < y will always return true.
        x > y will always return false.
    else the opposite will happen.

    x == y will always return false unless y is also an instance of Infinity 
    with the same sign."""

    def __init__(self, sign="+"):

        if sign != "+" and sign != "-":
            raise ValueError(f"{sign} is an invalid sign. The sign must either be '+' or '-'.")

        self.__sign = sign

    def get_sign(self):
        """Returns the sign of this infinity as a one character string: 
        
        '+' for positive infinity
        '-' for negative infinity"""

        return self.__sign

    def __lt__(self, other):
        """Returns the result of {self} < {other}. if the sign is negative, this object must
        return true for all comparisons (unless the {other} is also negative Infinity), false otherwise."""

        return self.__sign == "-" and not self == other 

    def __eq__(self, other):
        """Returns true if other is an instance of this class and has the same sign."""

        return isinstance(other, _Infinity) and self.__sign == other.get_sign()

class BinaryHeap:
    """This is a binary heap data structure."""

    __INIT_MAX_SIZE = 5

    def __init__(self, data=None, key=(lambda x: x)):
        """Constructor for a Binary (min) heap.

        {key} is a function that returns the value that is used during 
        comparisons (by default it is the element itself). The < operator is used
        when comparing values.

        (optional) Will add all the elements in {data} to the heap. 
        {data} must be an iterable object. O(N), N = size of the heap"""

        if not hasattr(key, "__call__"):
            raise ValueError("{key} must be a callable object")

        self.__size = 0
        self.__max_size = BinaryHeap.__INIT_MAX_SIZE
        self.__key = self.__infinity_if_none(key)

        self.__list = [None] + [None]*self.__max_size

        if hasattr(data, "__iter__"):  
            for elem in data:
                self.push(elem)
        elif data is not None:
            raise TypeError("Passed data is not an iterable.")

    def __len__(self):
        """Returns the size of the heap. O(1)"""
        
        return self.__size

    def __str__(self):
        """Returns a string representation of the heap. O(N), N = size of the heap"""
        
        return str(self.__list[1:(self.__size + 1)])

    def __iter__(self):
        """Returns an iterator for the elements in the heap. O(1)"""
        
        return iter(self.__list[1:(self.__size + 1)])

    def push(self, element):
        """Adds {element} to the heap. O(logN), N = size of the heap"""

        self.__size += 1

        if self.__size >= self.__max_size//2:
            self.__list += [None] * self.__max_size
            self.__max_size *= 2

        curr_index = self.__size
        self.__list[curr_index] = element

        self.__bubble_up(curr_index)

    def pop(self):
        """Removes and returns the first element in the heap. O(logN), N = size of the heap"""

        if self.__size == 0: 
            raise Exception("There are no elements in the heap.")

        data = self.__list[1]
        self.__swap_nodes(1, self.__size)
        self.__list[self.__size] = None

        self.__size -= 1

        curr_index = 1
        self.__bubble_down(curr_index)

        return data

    def peek(self):
        """Returns the first element in the heap. O(1)"""

        if self.__size == 0: 
            raise Exception("There are no elements in the heap.")

        return self.__list[1]

    def remove(self, element):
        """Removes {element} from the heap, if it exists. 
        Returns True if {element} was removed. O(N)"""

        for i in range(1, self.__size + 1):
            if self.__list[i] == element:

                self.__swap_nodes(i, self.__size)
                self.__list[self.__size] = None
                self.__size -= 1
                
                self.__bubble_down(i)

                return True

        return False

    def __infinity_if_none(self, key):

        def wrapper(data):

            if data is None:
                return _Infinity(sign="+")
            else:
                return key(data)

        return wrapper

    def __parent(self, index):
        """Returns the index of the parent for node at {index}."""

        return index // 2

    def __left_child(self, index):
        """Returns the index of the left child for node at {index}."""

        return index * 2

    def __right_child(self, index):
        """Returns the index of the right child for node at {index}."""

        return index * 2 + 1

    def __bubble_up(self, index):
        """Moves the node at {index} up the heap until the heap invariant is restored."""

        while index > 1:

            parent_index = self.__parent(index) 

            if self.__key(self.__list[index]) < self.__key(self.__list[parent_index]):
                
                self.__swap_nodes(index, parent_index)
                index = parent_index
            else:
                break

    def __bubble_down(self, index):
        """Moves the node at {index} down the heap until the heap invariant is restored."""

        while index <= self.__size:

            curr_value = self.__key(self.__list[index])
            left_child = self.__left_child(index)
            right_child = self.__right_child(index)

            if self.__key(self.__list[left_child]) < self.__key(self.__list[right_child]):
                
                min_value = self.__key(self.__list[left_child])
                min_index = left_child
            else:
                min_value = self.__key(self.__list[right_child])
                min_index = right_child

            if min_value < curr_value:
                
                self.__swap_nodes(index, min_index)
                index = min_index
            else:
                break

    def __swap_nodes(self, left_node, right_node):
        """Swaps the contents between {left_node} and {right_node}."""

        self.__list[left_node], self.__list[right_node] = self.__list[right_node], self.__list[left_node]
        