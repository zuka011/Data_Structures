

class LinkedList():
    """A singly linked list data structure."""

    def __init__(self, data=None):
        """Constructor for Linked List. O(N), N = #elements in {data}

        (optional) Will add elements in {data} to the list. {data} must be an iterable object.
        """

        self.head = None
        self.tail = None
        self.elem_count = 0

        if hasattr(data, "__iter__"):  
            for elem in data:
                self.push_back(elem)
        elif data is not None:
            raise TypeError("Passed data is not an iterable.")

    def __len__(self):
        """Returns number of elements in the list. O(1)"""

        return self.elem_count

    def __str__(self):
        """Returns a string representation of the list. O(N), N = #elements in list"""

        string_representation = ""

        curr_node = self.head
        while curr_node is not None:
            
            if type(curr_node.data) is str: 
                string_representation = ", ".join((string_representation, "".join(("'", curr_node.data, "'"))))
            else:
                string_representation = ", ".join((string_representation, str(curr_node.data)))
            
            curr_node = curr_node.next

        return "".join(("[", string_representation[2:], "]"))

    def __iter__(self):
        """Returns an iterator for this linked list. O(1)"""
        
        self.__curr_node = self.head
        return self

    def __next__(self):
        """Returns the next item in the iterator."""

        if self.__curr_node is not None:

            data = self.__curr_node.data
            self.__curr_node = self.__curr_node.next
            return data
        else:
            raise StopIteration

    def push_back(self, data):
        """Adds an element to the end of the list."""

        raise NotImplementedError

    def push_front(self, data):
        """Adds an element to the start of the list."""

        raise NotImplementedError

    def pop_back(self):
        """Removes and returns an element from the end of the list."""

        raise NotImplementedError

    def pop_front(self):
        """Removes and returns an element from the start of the list."""
        
        raise NotImplementedError

    def peek_back(self):
        """Returns the element at the end of the list. O(1)"""

        if self.elem_count == 0:
            raise Exception("There are no elements in this list.")

        return self.tail.data

    def peek_front(self):
        """Returns the element at the start of the list. O(1)"""

        if self.elem_count == 0:
            raise Exception("There are no elements in this list.")
        
        return self.head.data

