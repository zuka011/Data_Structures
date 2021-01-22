import sys
sys.path.append(r"..")

import unittest
from Data_Structures.fenwick_tree import FenwickTree


class TestFenwickTree(unittest.TestCase):

    def test_constructor(self):
        
        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        f_tree = FenwickTree(5, (1, 2, 3))

        with self.assertRaises(TypeError):
            f_tree = FenwickTree(1, 1)

        with self.assertRaises(Exception):
            f_tree = FenwickTree(-1)

    def test_len(self):

        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        self.assertEqual(len(f_tree), 5)

        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        self.assertEqual(len(f_tree), 5)
        
        f_tree = FenwickTree(5, (1, 2, 3))
        self.assertEqual(len(f_tree), 5)

    def test_str(self):

        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        self.assertEqual(str(f_tree), "[1, 2, 3, 4, 5]")

        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        self.assertEqual(str(f_tree), "[1, 2, 3, 4, 5]")
        
        f_tree = FenwickTree(5, (1, 2, 3))
        self.assertEqual(str(f_tree), "[1, 2, 3, 0, 0]")

    def test_iter(self):

        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, 3, 3, 10, 5])

        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, 3, 3, 10, 5])

        f_tree = FenwickTree(5, (1, 2, 3))
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, 3, 3, 6, 0])

    def test_update_point(self):

        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        f_tree.update_point(1, 4)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [5, 7, 3, 14, 5])

        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        f_tree.update_point(2, -2)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, 1, 3, 8, 5])

        f_tree = FenwickTree(5, (1, 2, 3))
        f_tree.update_point(5, 5)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, 3, 3, 6, 5])

        f_tree = FenwickTree(30)
        data = [i for i in range(0, 30)]
        self.__update_points(f_tree, 0, 30, data)

        data = list(map(lambda x: -x, data))
        self.__update_points(f_tree, 0, 30, data)

        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [0] * 30)

        with self.assertRaises(IndexError):

            f_tree = FenwickTree(10)
            f_tree.update_point(-1, 10)

    def test_set_point(self):

        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        f_tree.set_point(1, 4)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [4, 6, 3, 13, 5])

        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        f_tree.set_point(2, -2)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, -1, 3, 6, 5])

        f_tree = FenwickTree(5, (1, 2, 3))
        f_tree.set_point(5, 5)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [1, 3, 3, 6, 5])

        f_tree = FenwickTree(30)
        data = [i for i in range(0, 30)]
        self.__set_points(f_tree, 0, 30, data)

        data = list(map(lambda x: -x, data))
        self.__set_points(f_tree, 0, 30, data)

        self.__set_points(f_tree, 0, 30, [0] * 30)
        working_values = [elem for elem in f_tree]
        self.assertEqual(working_values, [0] * 30)

        with self.assertRaises(IndexError):

            f_tree = FenwickTree(10)
            f_tree.set_point(-1, 10)

    def test_get_sum(self):

        f_tree = FenwickTree(5, [1, 2, 3, 4, 5])
        self.assertEqual(f_tree.get_sum(1, 1), 1)
        self.assertEqual(f_tree.get_sum(1, 5), 15)
        self.assertEqual(f_tree.get_sum(3, 5), 12)

        f_tree = FenwickTree(3, [1, 2, 3, 4, 5])
        self.assertEqual(f_tree.get_sum(1, 1), 1)
        self.assertEqual(f_tree.get_sum(1, 5), 15)
        self.assertEqual(f_tree.get_sum(3, 5), 12)

        f_tree = FenwickTree(5, (1, 2, 3))
        self.assertEqual(f_tree.get_sum(1, 1), 1)
        self.assertEqual(f_tree.get_sum(1, 5), 6)
        self.assertEqual(f_tree.get_sum(3, 5), 3)

        with self.assertRaises(IndexError):

            f_tree = FenwickTree(2)
            f_tree.get_sum(1, 10)

        with self.assertRaises(IndexError):

            f_tree = FenwickTree(10)
            f_tree.get_sum(-1, 10)

    def __update_points(self, f_tree, start_index, end_index, data):

        if end_index - start_index != len(data):
            raise Exception("There's a problem with the tests.")

        starting_values = f_tree.get_elements()

        for i in range(start_index, end_index):
            f_tree.update_point(i + 1, data[i - start_index])

        ending_values = f_tree.get_elements()
        difference = list(map(lambda x, y: x - y, ending_values, starting_values))

        self.assertEqual(difference[start_index:end_index], data)

    def __set_points(self, f_tree, start_index, end_index, data):

        if end_index - start_index != len(data):
            raise Exception("There's a problem with the tests.")

        for i in range(start_index, end_index):
            f_tree.set_point(i + 1, data[i - start_index])

        ending_values = f_tree.get_elements()

        self.assertEqual(ending_values[start_index:end_index], data)
   

if __name__ == "__main__":
    unittest.main()