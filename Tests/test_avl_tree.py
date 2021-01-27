from datetime import date
import sys

sys.path.append(r"..")

import unittest
from random import randint
from random import choice as random_choice
from string import ascii_letters

from Source.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def test_constructor(self):
        
        avl_tree = AVLTree()
        avl_tree = AVLTree([1, 2, 3, 4, 5])
        avl_tree = AVLTree((1, 2, 3))
        avl_tree = AVLTree([(3, 1), (1, 2), (5,)], lambda x: x[0])

        with self.assertRaises(TypeError):
            avl_tree = AVLTree(1)

        with self.assertRaises(ValueError):
            avl_tree = AVLTree((1, 2), 5)

    def test_len(self):

        avl_tree = AVLTree()
        self.assertEqual(len(avl_tree), 0)

        avl_tree = AVLTree((1, 2, 3))
        self.assertEqual(len(avl_tree), 3)

        avl_tree = AVLTree([1, 2, 3, 4, 5])
        self.assertEqual(len(avl_tree), 5)
        
        avl_tree = AVLTree([(3, 1), (1, 2), (5,)], lambda x: x[0])
        self.assertEqual(len(avl_tree), 3)

    def test_str(self):

        avl_tree = AVLTree()
        self.assertEqual(str(avl_tree), "[]")

        avl_tree = AVLTree((1, 2))
        self.assertEqual(str(avl_tree), str([1, 2]))

        avl_tree = AVLTree((1, 2, 3))
        self.assertEqual(str(avl_tree), str([1, 2, 3]))

        avl_tree = AVLTree([1, 2, 3, 4, 5])
        self.assertEqual(str(avl_tree), str([1, 2, 3, 4, 5]))

        avl_tree = AVLTree([(3, 1), (1, 2), (5,)], lambda x: x[0])
        self.assertEqual(str(avl_tree), str([(1, 2), (3, 1), (5,)]))

    def test_iter(self):

        avl_tree = AVLTree()
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [])

        avl_tree = AVLTree((1, 2))
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [1, 2])

        avl_tree = AVLTree((1, 2, 3))
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [1, 2, 3])

        avl_tree = AVLTree([1, 2, 3, 4, 5])
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [1, 2, 3, 4, 5])

        avl_tree = AVLTree([(3, 1), (1, 2), (5,)], lambda x: x[0])
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [(1, 2), (3, 1), (5,)])

    def test_add(self):

        avl_tree = AVLTree()
        avl_tree.add(5)
        avl_tree.add(1)
        avl_tree.add(3)
        working_values = [elem for elem in avl_tree]
        self.assertEqual(sorted(working_values), [1, 3, 5])

        avl_tree = AVLTree([3, 1, 2, 2, 3])
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [1, 2, 2, 3, 3])

        avl_tree = AVLTree((3, 1,  2))
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, [1, 2, 3])

        avl_tree = AVLTree()
        data = [randint(0, 100) for _ in range(200)]
        self.__add_elems(avl_tree, data)
        self.assertEqual([elem for elem in avl_tree], sorted(data))
        working_values1 = [elem for elem in avl_tree]

        avl_tree = AVLTree()
        self.__add_elems(avl_tree, data[::-1])
        self.assertEqual([elem for elem in avl_tree], sorted(data))
        working_values2 = [elem for elem in avl_tree]

        self.assertEqual(working_values1, working_values2)

        avl_tree = AVLTree()
        data = ["".join([random_choice(ascii_letters) for _ in range(randint(1, 10))]) for _ in range(20)]
        self.__add_elems(avl_tree, data)
        working_values = [elem for elem in avl_tree]
        self.assertEqual(working_values, sorted(data))

    def test_remove(self):

        avl_tree = AVLTree([1, 2, 3, 4, 5])

        for i in range(1, 6):
            self.assertEqual(avl_tree.remove(i), True)
            self.assertEqual(avl_tree.remove(5 + i), False)

        self.assertEqual(len(avl_tree), 0)

        data = [1, 2, 3, 4, 6, 7, 10]
        avl_tree = AVLTree([1, 6, 2, 7, 10, 3, 4])
        
        self.assertEqual(avl_tree.remove(7), True)

        avl_tree = AVLTree([(1, 2), (5, 6), (3, 4)], lambda x: x[0])
        self.assertEqual(avl_tree.remove((1, 2)), True)
        self.assertEqual(avl_tree.remove((3, 4)), True)

        self.assertEqual([elem for elem in avl_tree], [(5, 6)])

        self.assertEqual(avl_tree.remove((5, 6)), True)
        self.assertEqual(len(avl_tree), 0)

        data = [randint(0, 100) for _ in range(200)]
        avl_tree = AVLTree(data)
        self.__remove_elems(avl_tree, data)

        data = ["".join([random_choice(ascii_letters) for _ in range(randint(1, 10))]) for _ in range(20)]
        avl_tree = AVLTree(data)
        self.__remove_elems(avl_tree, data)

    def test_contains(self):

        data = [randint(0, 100) for _ in range(200)]
        avl_tree = AVLTree(data)

        for elem in data:
            self.assertEqual(avl_tree.contains(elem), True)

        excluded_data = [randint(101, 1000) for _ in range(200)]
        for elem in excluded_data:
            self.assertEqual(avl_tree.contains(elem), False)

        data = ["".join([random_choice(ascii_letters) for _ in range(randint(1, 10))]) for _ in range(20)]
        avl_tree = AVLTree(data)

        for elem in data:
            self.assertEqual(avl_tree.contains(elem), True)

    def test_integration(self):

        random_data_size_1 = 100
        random_data_size_2 = 200

        avl_tree = AVLTree()
        data_1 = [randint(0, 100) for _ in range(random_data_size_1)] 
        data_2 = [randint(101, 1000) for _ in range(random_data_size_2)]

        self.__add_elems(avl_tree, data_1)
        self.assertEqual(len(avl_tree), random_data_size_1)

        for elem in data_1:
            self.assertEqual(avl_tree.contains(elem), True)

        for elem in data_2:
            self.assertEqual(avl_tree.contains(elem), False)

        self.__add_elems(avl_tree, data_2)
        self.assertEqual(len(avl_tree), random_data_size_1 + random_data_size_2)

        for elem in data_2:
            self.assertEqual(avl_tree.contains(elem), True)

        self.assertEqual([elem for elem in avl_tree], sorted(data_1 + data_2))

        self.__remove_elems(avl_tree, data_1)
        self.assertEqual(len(avl_tree), random_data_size_2)

        for elem in data_2:
            self.assertEqual(avl_tree.contains(elem), True)

        for elem in data_1:
            self.assertEqual(avl_tree.contains(elem), False)
            
        self.__remove_elems(avl_tree, data_2)
        self.assertEqual(len(avl_tree), 0)

    def __add_elems(self, avl_tree, data):

        for elem in data:
            avl_tree.add(elem)

    def __remove_elems(self, avl_tree, data):

        starting_length = len(avl_tree)

        for elem in data:
            self.assertEqual(avl_tree.remove(elem), True)

        self.assertEqual(starting_length - len(avl_tree), len(data))
    

if __name__ == "__main__":
    unittest.main()
