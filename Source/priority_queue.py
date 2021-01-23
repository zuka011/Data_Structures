import sys

sys.path.append(r"..")

from Source.binary_heap import BinaryHeap


class PriorityQueue(BinaryHeap):
    """This is a (min) priority queue data structure.

    This implementation uses a binary heap."""

    def __init__(self, data=None, key=(lambda x: x)):
        """Constructor for the (min) priority queue.

        {key} is a function that returns the value that is used during 
        comparisons (by default it is the element itself). The < operator is used
        when comparing values.

        (optional) Will add all the elements in {data} to the queue. 
        {data} must be an iterable object. O(N), N = size of the queue"""

        super().__init__(data, key)

    def __iter__(self):
        """Returns an iterator for the elements in the queue. O(1)"""
        
        return self

    def __next__(self):
        """Returns the next element in the iterator."""

        if self:
            return self.pop()
        else:
            raise StopIteration
