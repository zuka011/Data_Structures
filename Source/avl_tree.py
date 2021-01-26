

from typing import Iterable, Iterator


class _AVLTreeNode:
    """This is a node structure for the AVL tree."""

    def __init__(self, data, parent=None, left=None, right=None):
        
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
        self.balance_factor = 0


class AVLTree:
    """This is a Balanced Binary Search Tree structure.
    
    This implementation allows for duplicate values."""

    def __init__(self, data: Iterable=None, key=lambda x: x):
        """Constructor for an AVL tree.

        (optional) {key} is a function that returns the parameter 
        which is used during comparisons. The < operator is used 
        when comparing keys of elements. By default the key of the
        elements are themselves.

        (optional) {data} will be inserted into the AVL tree. 
        {data} must be an iterable object. O(N*logN), N = size of the tree"""

        if not hasattr(key, "__call__"):
            raise ValueError("{key} must be a callable object")

        self.__root = None
        self.__size = 0
        self.__key = key

        if hasattr(data, "__iter__"):
            for element in data:
                self.add(element)
        elif data is not None:
            raise TypeError("Data must be an iterable object.")

    def __len__(self) -> int:
        """Returns the number of elements in the tree. O(1)"""

        return self.__size

    def __str__(self) -> str:
        """Returns a string representation of the elements in this structure.
        The elements will be sorted in ascending order. O(N), N = size of the tree"""

        elements = []
        self.__get_sorted_elements(self.__root, elements)

        return str(elements)

    def __iter__(self) -> Iterator:
        """Returns an iterator over all the elements in this structure.
        The elements will be sorted in ascending order. O(N), N = size of the tree"""

        elements = []
        self.__get_sorted_elements(self.__root, elements)

        return iter(elements)

    def add(self, element) -> None:
        """Adds an element to the tree. O(logN), N = size of the tree"""

        self.__root = self.__add_recursive(self.__root, element)
        self.__size += 1

        if not self.__is_balanced(self.__root):
            raise AssertionError("This AVL Tree is not balanced any more.")

    def remove(self, element) -> bool:
        """Removes the element from the tree if it exists. Returns
        True if the element was succesfully removed, false otherwise. 
        O(logN), N = size of the tree"""

        removed_node = self.__find_node(element)

        if removed_node is None:
            return False

        self.__size -= 1

        # return True
        pass

    def __remove_leaf_node(self, leaf_node: _AVLTreeNode):
        pass

    def contains(self, element) -> bool:
        """Returns true if the element is in the tree, false otherwise.
        O(logN), N = size of the tree"""

        return self.__find_node(element) is not None 

    def map(self, map_function, *map_arguments) -> None:
        """Iterates over all the elements in the tree and calls 
        {map_function} for each. The elements of this tree will always
        be the first argument. {map_arguments} will also be passed
        to {map_function} if specified."""

        elements = []
        self.__get_sorted_elements(self.__root, elements)

        for element in elements:
            map_function(element, *map_arguments)

    def __is_balanced(self, curr_node: _AVLTreeNode or None):
        """Checks if the AVL Tree is balanced (For debugging purpoes)."""

        if curr_node is None:
            return True

        return abs(curr_node.balance_factor) < 2 \
                and self.__is_balanced(curr_node.left) and self.__is_balanced(curr_node.right)

    def __find_node(self, element) -> _AVLTreeNode or None:
        """Returns a pointer to the node that stores {element}, or
        None if such a node doesn't exist. O(logN), N = size of the tree"""

        curr_node = self.__root
        while curr_node is not None:

            if self.__key(element) < self.__key(curr_node.data):
                curr_node = curr_node.left
            elif self.__key(curr_node.data) < self.__key(element):
                curr_node = curr_node.right
            else:
                return curr_node

        return None

    def __add_recursive(self, curr_node: _AVLTreeNode or None, element):
        """Adds a node containing {element} to the AVL Tree with 
        root {curr_node} and returns a pointer to the new root of
        the tree. O(logN), N = size of the tree"""

        if curr_node is None:
            return  _AVLTreeNode(element)

        if self.__key(element) < self.__key(curr_node.data):
            curr_node.left = self.__add_recursive(curr_node.left, element)
            curr_node.left.parent = curr_node
        else:
            curr_node.right = self.__add_recursive(curr_node.right, element)
            curr_node.right.parent = curr_node

        self.__update(curr_node)
        return self.__balance(curr_node)

    def __left_rotation(self, node: _AVLTreeNode) -> _AVLTreeNode:
        """Performs a left rotation on {node}."""

        right_node = node.right

        if right_node.left is not None:
            right_node.left.parent = node

        node.right = right_node.left
        right_node.left = node

        right_node.parent = node.parent
        node.parent = right_node

        self.__update(node)
        self.__update(right_node)

        return right_node

    def __right_rotation(self, node: _AVLTreeNode) -> _AVLTreeNode:
        """Performs a right rotation on {node}."""
        
        left_node = node.left

        if left_node.right is not None:
            left_node.right.parent = node

        node.left = left_node.right
        left_node.right = node

        left_node.parent = node.parent
        node.parent = left_node

        self.__update(node)
        self.__update(left_node)

        return left_node

    def __balance(self, node: _AVLTreeNode) -> _AVLTreeNode:
        """Balances {node} if required."""

        if node.balance_factor == 2:

            if node.right.balance_factor == 1:
                node = self.__left_rotation(node)
            else:
                node.right = self.__right_rotation(node.right)
                node = self.__left_rotation(node)

        elif node.balance_factor == -2:

            if node.left.balance_factor == -1:
                node = self.__right_rotation(node)
            else:
                node.left = self.__left_rotation(node.left)
                node = self.__right_rotation(node)

        return node

    def __update(self, node: _AVLTreeNode) -> None:
        """Updates the height and balance factor for {node}."""

        left_height = self.__get_node_height(node.left)
        right_height = self.__get_node_height(node.right)

        node.height = max(left_height, right_height) + 1
        node.balance_factor = right_height - left_height

    def __get_node_height(self, node: _AVLTreeNode or None) -> int:
        """Returns the height of {node} or -1 if it is None."""

        if node is None:
            return -1
        else:
            return node.height

    def __get_sorted_elements(self, curr_node: _AVLTreeNode, elements: list) -> None:
        """Recursive function that will retrieve all elements in the tree
        with root {curr_node} and place them in {elements} in ascending 
        sorted order."""

        if curr_node is None:
            return

        self.__get_sorted_elements(curr_node.left, elements)
        elements.append(curr_node.data)
        self.__get_sorted_elements(curr_node.right, elements)



