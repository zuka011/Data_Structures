

class BinaryHeap:
    """This is a binary heap data structure."""

    def __init__(self, size=None, key=(lambda x: x), data=None):
        """Creates a Binary heap of size max({size}, #elements in {data}).

        Either {size} or {data} must be specified.

        {key} is a function that returns the value that is used during 
        comparisons (by default it is the element itself). The < operator is used
        when comparing values.

        (optional) Will add all the elements in {data} to the heap. 
        {data} must be an iterable object. O(N), N = size of the heap"""

        pass

    def __len__(self):
        """Returns the size of the heap. O(1)"""
        pass

    def __str__(self):
        """Returns a string representation of the heap. O(N), N = size of the heap"""
        pass

    def __iter__(self):
        """Returns an iterator for the elements in the heap. O(1)"""
        pass

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