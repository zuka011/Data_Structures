

class FenwickTree:
    """This is a Fenwick Tree structure."""

    def __init__(self, size=None, data=None):
        """Creates a Fenwick Tree structure of size max({size}, #elements in {data}).

        Either {size} or {data} must be specified.

        (Optional) will add all the elements in {data} to the Fenwick Tree. 
        {data} must be iterable. O(N), N = max index in Fenwick Tree"""

        if size is None:
            if data is None: 
                raise Exception("You need to specify the size of the Fenwick Tree.")
        elif size <= 0:
            raise Exception("You can't have a Fenwick Tree of non-positive size.")

        self.__check_data(data)
        
        if data is None:
            self.__list = [None] + [0] * size
            self.__size = size
        else:    
            self.__list = [None] + [elem for elem in data] + [0] * (size - len(data))  
            self.__size = max(size, len(data))

        self.__construct_tree()

    def __len__(self):
        """Returns the number of indices in the Fenwick Tree. O(1)"""

        return self.__size

    def __str__(self):
        """Returns a string representation of the elements in the Fenwick Tree. 
        O(N*logN), N = max index in Fenwick Tree"""
            
        string_representation = ""

        for i in range(1, self.__size + 1):
            string_representation = ", ".join((string_representation, str(self.get_sum(i, i))))

        return "".join(("[", string_representation[2:], "]"))

    def __iter__(self):
        """Returns an iterator to the working values in this Fenwick Tree."""

        return iter(self.__list[1:])

    def get_elements(self):
        """Returns the elements in the Fenwick Tree as a list.
        O(N*logN), N = max index in Fenwick Tree"""

        return [self.get_sum(i, i) for i in range(1, self.__size + 1)]

    def update_point(self, index, difference):
        """Adds {difference} to the element at {index} in the Fenwick Tree.
        O(logN), N = max index in Fenwick Tree
        
        Indexing is 1 based."""

        self.__check_bounds(index)

        while index <= self.__size:

            self.__list[index] += difference
            index += self.__lsb(index)

    def set_point(self, index, new_value):
        """Sets the element at {index} to {new_value}. O(logN), N = # elements in data.
        O(logN), N = max index in Fenwick Tree
        
        Indexing is 1 based."""

        self.__check_bounds(index)
        difference = new_value - self.get_sum(index, index)
        
        self.update_point(index, difference)

    def get_sum(self, start_index, end_index):
        """Returns the sum of all elements in the range [{start_index}, {end_index}]. O(1)
        
        Indexing is 1 based."""

        self.__check_bounds(start_index)
        self.__check_bounds(end_index)

        return self.__prefix_sum(end_index) - self.__prefix_sum(start_index - 1) 

    def __check_data(self, data):
        """Checks the data passed to the constructor to make sure it is either empty or 
        an iterable object containing integers or floats."""

        if data is not None:
            if hasattr(data, "__iter__"):

                for elem in data: 
                    if type(elem) is not int and type(elem) is not float:
                        raise TypeError("Elements in data must be either integers or floats.")
            else:
                raise TypeError("Passed data is not an iterable.")

    def __construct_tree(self):
        """Constructs the Fenwick Tree according to the data passed to it's constructor.
        O(N), N = max index in Fenwick Tree"""
        
        for index in range(1, self.__size + 1):

            parent_index = index + self.__lsb(index)

            if parent_index <= self.__size: 
                self.__list[parent_index] += self.__list[index]

    def __prefix_sum(self, end_index):
        """Returns the sum of all elements in the range [1, {end_index}]. O(1)"""

        curr_sum = 0

        while end_index > 0:
            
            curr_sum += self.__list[end_index]
            end_index -= self.__lsb(end_index)

        return curr_sum

    def __check_bounds(self, index):
        """Raises an error if index {index} is out of the Fenwick Tree's bounds.""" 

        if index < 1 or index > self.__size:
            raise IndexError(f"Index {index} is out of bounds. Value should be between [1, {self.__size}].")

    def __lsb(self, index):
        """Returns the a number with only the least significant bit of {index} set."""

        return index & -index
