import sys

sys.path.append(r"..")

from Source.linked_list import LinkedList


class _LinkedListNode():
    """A node structure for a doubly linked list."""

    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList(LinkedList):
    """A doubly linked list data structure."""

    def __init__(self, data=None):
        """Constructor for Linked List. O(N), N = #elements in {data}

        (optional) Will add elements in {data} to the list. {data} must be an iterable object.
        """

        super().__init__(data)

    def push_back(self, data) -> None:
        """Adds an element to the end of the list. O(1)"""

        self.elem_count += 1
        
        if self.head is None: 
            
            self.head = _LinkedListNode(data)
            self.tail = self.head
        else:

            newNode = _LinkedListNode(data, previous=self.tail)
            self.tail.next = newNode
            self.tail = newNode

    def push_front(self, data) -> None:
        """Adds an element to the start of the list. O(1)"""

        self.elem_count += 1
        
        if self.head is None: 
            
            self.head = _LinkedListNode(data)
            self.tail = self.head
        else:

            newNode = _LinkedListNode(data, next=self.head)
            self.head.previous = newNode
            self.head = newNode

    def pop_back(self):
        """Removes and returns an element from the end of the list. O(1)"""

        if self.elem_count == 0:
            raise Exception("There are no elements in this list.")
        
        self.elem_count -= 1

        data = self.tail.data
        self.tail = self.tail.previous
        
        if self.tail is not None:
            self.tail.next = None

        return data

    def pop_front(self):
        """Removes and returns an element from the start of the list. O(1)"""
        
        if self.elem_count == 0:
            raise Exception("There are no elements in this list.")

        self.elem_count -= 1

        data = self.head.data
        self.head = self.head.next

        if self.head is not None:
            self.head.previous = None

        return data

    def remove(self, target) -> bool:
        """Removes {target} from the linked list if it is present. 
        Equality is determined by the == operator. Returns True if 
        the element is present in the list. O(N), N = #elements in the list"""

        curr_node = self.head

        while curr_node is not None:

            if curr_node.data == target:
                
                if curr_node is self.head:
                    self.head = curr_node.next

                if curr_node is self.tail:
                    self.tail = curr_node.previous

                if curr_node.previous is not None:
                    curr_node.previous.next = curr_node.next
                
                if curr_node.next is not None:
                    curr_node.next.previous = curr_node.previous

                self.elem_count -= 1

                return True
            
            curr_node = curr_node.next

        return False

    def contains(self, target) -> bool:
        """Returns true if {element} is present in the list. Equality
        is determined by the == operator. O(N), N = #elements in the list"""

        for element in self:
            if element == target:
                return True

        return False
        
