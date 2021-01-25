import sys

sys.path.append(r"..")

import unittest
from random import randint

from Source.union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_constructor(self):
        
        u_find = UnionFind()
        u_find = UnionFind(10)
        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        u_find = UnionFind(data=["cat", "dog", [1, 2]])

    def test_len(self):

        u_find = UnionFind()
        self.assertEqual(len(u_find), 0)
        
        u_find = UnionFind(10)
        self.assertEqual(len(u_find), 10)

        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        self.assertEqual(len(u_find), 5)

        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        self.assertEqual(len(u_find), 10)

        u_find = UnionFind(data=["cat", "dog", [1, 2]])
        self.assertEqual(len(u_find), 3)

    def test_str(self):

        u_find = UnionFind()
        self.assertEqual(str(u_find), "[]")
        
        u_find = UnionFind(10)
        self.assertEqual(str(u_find), str([(None, i) for i in range(1, 11)]))

        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        self.assertEqual(str(u_find), str([(i, i) for i in range(1, 6)]))

        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        self.assertEqual(str(u_find), str([(i, i) for i in range(1, 6)] + [(None, i) for i in range(6, 11)]))

        u_find = UnionFind(data=["cat", "dog", [1, 2]])
        self.assertEqual(str(u_find), "[('cat', 1), ('dog', 2), ([1, 2], 3)]")

    def test_iter(self):

        u_find = UnionFind()
        working_values = [pair for pair in u_find]
        self.assertEqual(working_values, [])
        
        u_find = UnionFind(10)
        working_values = [pair for pair in u_find]
        self.assertEqual(working_values, [(None, i) for i in range(1, 11)])

        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        working_values = [pair for pair in u_find]
        self.assertEqual(working_values, [(i, i) for i in range(1, 6)])

        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        working_values = [pair for pair in u_find]
        self.assertEqual(working_values, [(i, i) for i in range(1, 6)] + [(None, i) for i in range(6, 11)])

        u_find = UnionFind(data=["cat", "dog", [1, 2]])
        working_values = [pair for pair in u_find]
        self.assertEqual(working_values, [('cat', 1), ('dog', 2), ([1, 2], 3)])

    def test_add_element(self):
        
        u_find = UnionFind()
        data = [randint(0, 100) for i in range(50)]
        self.__add_elems(u_find, data)

        u_find = UnionFind(10)
        data = [randint(0, 100) for i in range(50)]
        self.__add_elems(u_find, data)
        self.assertEqual([pair[0] for pair in u_find][:10], [None] * 10)

        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        data = [randint(0, 100) for i in range(50)]
        self.__add_elems(u_find, data)

        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        data = [randint(0, 100) for i in range(50)]
        self.__add_elems(u_find, data)

        u_find = UnionFind(data=["cat", "dog", [1, 2]])
        data = [randint(0, 100) for i in range(50)]
        self.__add_elems(u_find, data)
        self.__add_elems(u_find, data)

    def test_set_element(self):

        u_find = UnionFind(100)
        data_pairs = [(i, randint(0, 300)) for i in range(1, 101)]
        self.__set_elems(u_find, data_pairs)

        u_find = UnionFind(100, [None] * 10)
        data_pairs = [(i, randint(0, 300)) for i in range(11, 101)]
        self.__set_elems(u_find, data_pairs)
        
        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        data_pairs = [(i, randint(0, 300)) for i in range(6, 101)]
        self.__set_elems(u_find, data_pairs)

        with self.assertRaises(IndexError):
            
            u_find = UnionFind(10)
            u_find.set_element(12, None)

        with self.assertRaises(IndexError):
            
            u_find = UnionFind(10)
            u_find.set_element(0, None)

    def test_merge(self):
        
        u_find = UnionFind(data=[randint(0, 100) for i in range(1, 11)])
        
        # Merge all odd indices together
        self.__merge_into_group(u_find, [i for i in range(1, 11, 2)])

        # Merge all even indices together
        self.__merge_into_group(u_find, [i for i in range(2, 11, 2)])

        # Merge the above two groups
        self.__merge_pairs(u_find, [(1, 2)])
        self.assertEqual(len(u_find), 1)

        # Manual Test
        u_find = UnionFind(data=[randint(0, 100) for i in range(1, 11)])

        self.__merge_pairs(u_find, [(1, 3), (5, 7), (2, 4), (6, 8)])
        self.assertEqual(len(u_find), 6)

        self.__merge_pairs(u_find, [(9, 10)])
        self.assertEqual(len(u_find), 5)

        self.__merge_pairs(u_find, [(1, 5), (2, 6)])
        self.assertEqual(len(u_find), 3)

        self.__merge_pairs(u_find, [(7, 3), (8, 4)])
        self.assertEqual(len(u_find), 3)

        self.__merge_pairs(u_find, [(7, 2)])
        self.assertEqual(len(u_find), 2)

        self.__merge_pairs(u_find, [(8, 1)])
        self.assertEqual(len(u_find), 2)

        self.__merge_pairs(u_find, [(10, 2)])
        self.assertEqual(len(u_find), 1)
        
    def test_is_same_group(self):
        
        u_find = UnionFind(data=[randint(0, 100) for i in range(1, 11)])
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(1, 11)]), False)
        
        # Merge all odd indices together (followed by a check)
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(1, 11, 2)]), False)
        self.__merge_into_group(u_find, [i for i in range(1, 11, 2)])
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(1, 11, 2)]), True)

        # Merge all even indices together (followed by a check)
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(2, 11, 2)]), False)
        self.__merge_into_group(u_find, [i for i in range(2, 11, 2)])
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(2, 11, 2)]), True)

        # Merge the above two groups (followed by a check)
        self.__merge_pairs(u_find, [(1, 2)])
        self.assertEqual(len(u_find), 1)
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(1, 11)]), True)

        # Manual Test (followed by checks)
        u_find = UnionFind(data=[randint(0, 100) for i in range(1, 11)])
        self.assertEqual(self.__check_if_elems_in_group(u_find, [i for i in range(1, 11)]), False)

        self.__merge_pairs(u_find, [(1, 3), (5, 7), (2, 4), (6, 8)])
        self.assertEqual(len(u_find), 6)
        self.__check_pairs(u_find, [(1, 3), (5, 7), (2, 4), (6, 8)])

        self.__merge_pairs(u_find, [(9, 10)])
        self.assertEqual(len(u_find), 5)
        self.__check_pairs(u_find, [(9, 10)])

        self.__merge_pairs(u_find, [(1, 5), (2, 6)])
        self.assertEqual(len(u_find), 3)
        self.__check_pairs(u_find, [(1, 5), (2, 6)])

        self.__merge_pairs(u_find, [(7, 3), (8, 4)])
        self.assertEqual(len(u_find), 3)
        self.__check_pairs(u_find, [(7, 3), (8, 4)])

        self.__merge_pairs(u_find, [(7, 2)])
        self.assertEqual(len(u_find), 2)
        self.__check_pairs(u_find, [(7, 2)])

        self.__merge_pairs(u_find, [(8, 1)])
        self.assertEqual(len(u_find), 2)
        self.__check_pairs(u_find, [(8, 1)])

        self.__merge_pairs(u_find, [(10, 2)])
        self.assertEqual(len(u_find), 1)
        self.__check_pairs(u_find, [(10, 2)])

    def __add_elems(self, u_find, data):

        starting_size = len(u_find)

        for elem in data: 
            u_find.add_element(elem)

        self.assertEqual(len(u_find) - starting_size, len(data))

        working_values = [pair for pair in u_find]
        self.assertEqual([pair[0] for pair in working_values[starting_size:]], data)

    def __set_elems(self, u_find, data_pairs):

        for pair in data_pairs:
            u_find.set_element(*pair)
        
        working_values = [pair for pair in u_find]
        for pair in data_pairs:
            self.assertEqual(working_values[pair[0] - 1][0], pair[1])

    def __merge_into_group(self, u_find, indices):

        initial_groups = len(u_find)
        group_reference = sorted(indices)[0]

        for index in indices:
            u_find.merge(index, group_reference)

        self.assertEqual(initial_groups - len(u_find), len(indices) - 1)

        working_values = [pair for pair in u_find]
        for index in indices:
            self.assertEqual(working_values[index - 1][1], group_reference)

    def __merge_pairs(self, u_find, index_pairs):

        for pair in index_pairs:
            u_find.merge(*pair)    

    def __check_if_elems_in_group(self, u_find, indices) -> bool:
        
        group_reference = sorted(indices)[0]

        for index in indices:
            if not u_find.is_same_group(index, group_reference):
                return False

        return True

    def __check_pairs(self, u_find, index_pairs):

        for pair in index_pairs:
            self.assertEqual(u_find.is_same_group(*pair), True)    


if __name__ == "__main__":
    unittest.main()
