import sys

sys.path.append(r"..")

from Source.singly_linked_list import SinglyLinkedList


class Queue:
    """A queue data structure.

    This implementations uses a singly linked list.
    """

    def __init__(self, data=None):
        """Constructor for the queue.

        (optional) enqueues elements in {data} into the queue. {data} must be an iterable object.
        O(N), N = #elements in {data}
        """

        self.__list = SinglyLinkedList(data)

    def __len__(self):
        """Returns the number of elements in the queue. O(1)"""

        return len(self.__list)

    def __str__(self):
        """Returns an easily readable string representation of the queue. O(N), N = #elements in data"""

        return str(self.__list)

    def __iter__(self):
        """Returns an iterator for this queue. O(1)"""

        return self

    def __next__(self):
        """Returns the next element in the iterator."""

        if self:
            return self.dequeue()
        else:
            raise StopIteration

    def enqueue(self, elem):
        """Adds an element to the end of the queue. O(1)"""

        self.__list.push_back(elem)

    def dequeue(self):
        """Removes and returns an element at the front of the queue. O(1)"""

        return self.__list.pop_front()

    def peek(self):
        """Returns the element at the front of the queue. O(1)"""

        return self.__list.peek_front()
