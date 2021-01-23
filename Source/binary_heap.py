

class BinaryHeap:
    """This is a binary heap data structure."""

    __INIT_MAX_SIZE = 5

    def __init__(self, data=None, key=(lambda x: x)):
        """Creates a Binary (min) heap from the elements in {data}.

        {key} is a function that returns the value that is used during 
        comparisons (by default it is the element itself). The < operator is used
        when comparing values.

        (optional) Will add all the elements in {data} to the heap. 
        {data} must be an iterable object. O(N), N = size of the heap"""

        self.__size = 0
        self.__max_size = BinaryHeap.__INIT_MAX_SIZE
        self.__key = key

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
        
        return self

    def __next__(self):
        """Returns the next element in the iterator."""

        if self:
            return self.pop()
        else:
            raise StopIteration

    def push(self, element):
        """Adds {element} to the heap. O(logN), N = size of the heap"""
        pass 

    def pop(self):
        """Removes and returns the first element in the heap. O(logN), N = size of the heap"""
        pass

    def peek(self):
        """Returns the first element in the heap. O(1)"""
        pass

    def remove(self, element):
        """Removes {element} from the heap, if it exists. O(N)"""
        pass