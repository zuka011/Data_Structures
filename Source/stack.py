import sys

sys.path.append(r"..")

from Source.singly_linked_list import SinglyLinkedList


class Stack:
    """A stack data structure.

    This implementations uses a singly linked list.
    """

    def __init__(self, data=None):
        """Constructor for the stack {data} structure.
        
        (optional) elements in {data} will be pushed into the stack. {data} must be an iterable object.
        O(N), N = #elements in {data}
        """

        if data is None:
            self.__list = SinglyLinkedList()
        elif hasattr(data, "__iter__"): 
            self.__list = SinglyLinkedList(data[::-1])
        else: 
            raise TypeError("Passed data is not an iterable.")

    def __len__(self):
        """Returns the number of elements in the stack. O(1)"""

        return len(self.__list)

    def __str__(self):
        """Returns an easily readable string representation of the stack. O(N), N = #elements in data"""

        return str(self.__list)

    def __iter__(self):
        """Returns an iterator for this stack. O(1)"""

        return self

    def __next__(self):
        """Returns the next item in the iterator."""

        if self:
            return self.pop()
        else:
            raise StopIteration

    def push(self, elem):
        """Adds an element to the top of the stack. O(1)"""

        self.__list.push_front(elem)

    def pop(self):
        """Removes and returns an element from the top of the stack. O(1)"""

        return self.__list.pop_front()

    def peek(self):
        """Returns the element at the top of the stack. O(1)"""

        return self.__list.peek_front()
