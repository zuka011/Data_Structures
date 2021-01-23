import sys

sys.path.append(r"..")

from Source.linked_list import LinkedList


class _LinkedListNode():
    """A node structure for a singly linked list."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList(LinkedList):
    """A singly linked list data structure."""

    def __init__(self, data=None):
        """Constructor for Linked List. O(N), N = #elements in {data}

        (optional) Will add elements in {data} to the list. {data} must be an iterable object.
        """

        super().__init__(data)

    def push_back(self, data):
        """Adds an element to the end of the list. O(1)"""

        self.elem_count += 1
        
        if self.head is None: 
            
            self.head = _LinkedListNode(data)
            self.tail = self.head
        else:

            newNode = _LinkedListNode(data)
            self.tail.next = newNode
            self.tail = newNode

    def push_front(self, data):
        """Adds an element to the start of the list. O(1)"""

        self.elem_count += 1
        
        if self.head is None: 
            
            self.head = _LinkedListNode(data)
            self.tail = self.head
        else:

            newNode = _LinkedListNode(data, self.head)
            self.head = newNode

    def pop_back(self):
        """Removes and returns an element from the end of the list. O(N), N = #elements in list"""

        if self.elem_count == 0:
            raise Exception("There are no elements in this list.")
        
        if self.elem_count == 1: 
            
            data = self.head.data
            self.head = None
            self.tail = None
            self.elem_count = 0

            return data

        self.elem_count -= 1

        curr_node = self.head

        while curr_node.next is not self.tail:
            curr_node = curr_node.next

        data = curr_node.next.data
        curr_node.next = None
        self.tail = curr_node

        return data

    def pop_front(self):
        """Removes and returns an element from the start of the list. O(1)"""
        
        if self.elem_count == 0:
            raise Exception("There are no elements in this list.")

        self.elem_count -= 1

        data = self.head.data
        self.head = self.head.next

        return data
