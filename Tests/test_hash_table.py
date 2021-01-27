from datetime import date
import sys

sys.path.append(r"..")

import unittest
from random import randint
from random import choice as random_choice
from string import ascii_letters

from Source.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def test_constructor(self):
        
        hash_table = HashTable()
        hash_table = HashTable(data=[1, 2, 3, 4, 5])
        hash_table = HashTable(data=(1, 2, 3))
        hash_table = HashTable(key=lambda x: x[0], data=[(3, 1), (1, 2), (5,)])

        with self.assertRaises(ValueError):
            hash_table = HashTable(data=1)

        with self.assertRaises(ValueError):
            hash_table = HashTable(data=(1, 2), hash_function=5)

    def test_len(self):

        hash_table = HashTable()
        self.assertEqual(len(hash_table), 0)

        hash_table = HashTable(data=(1, 2, 3))
        self.assertEqual(len(hash_table), 3)

        hash_table = HashTable(data=[1, 2, 3, 4, 5])
        self.assertEqual(len(hash_table), 5)
        
        hash_table = HashTable(data=[(3, 1), (1, 2), (5,)], key=lambda x: x[0])
        self.assertEqual(len(hash_table), 3)

    def test_str(self):

        hash_table = HashTable()
        self.assertEqual(str(hash_table), "[]")

        hash_table = HashTable(data=(1, 2))
        self.assertEqual(str(sorted(hash_table)), str([1, 2]))

        hash_table = HashTable(data=(1, 2, 3))
        self.assertEqual(str(sorted(hash_table)), str([1, 2, 3]))

        hash_table = HashTable(data=[1, 2, 3, 4, 5])
        self.assertEqual(str(sorted(hash_table)), str([1, 2, 3, 4, 5]))

        hash_table = HashTable(data=[(3, 1), (1, 2), (5,)], key=lambda x: x[0])
        self.assertEqual(str(sorted(hash_table, key=lambda x: x[0])), str([(1, 2), (3, 1), (5,)]))

    def test_iter(self):

        hash_table = HashTable()
        working_values = [elem for elem in hash_table]
        self.assertEqual(working_values, [])

        hash_table = HashTable(data=(1, 2))
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [1, 2])

        hash_table = HashTable(data=(1, 2, 3))
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [1, 2, 3])

        hash_table = HashTable(data=[1, 2, 3, 4, 5])
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [1, 2, 3, 4, 5])

        hash_table = HashTable(data=[(3, 1), (1, 2), (5,)], key=lambda x: x[0])
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [(1, 2), (3, 1), (5,)])

    def test_add(self):

        hash_table = HashTable()
        hash_table.add(5)
        hash_table.add(1)
        hash_table.add(3)
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [1, 3, 5])

        hash_table = HashTable(data=[3, 1, 2, 2, 3])
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [1, 2, 3])

        hash_table = HashTable(data=(3, 1,  2))
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), [1, 2, 3])

        hash_table = HashTable()
        data = [randint(0, 100) for _ in range(200)]
        self.__add_elems(hash_table, data)
        self.assertEqual(sorted([elem for elem in hash_table]), sorted(set(data)))
        working_values1 = [elem for elem in hash_table]

        hash_table = HashTable()
        self.__add_elems(hash_table, data[::-1])
        self.assertEqual(sorted([elem for elem in hash_table]), sorted(set(data)))
        working_values2 = [elem for elem in hash_table]

        self.assertEqual(sorted(working_values1), sorted(working_values2))

        hash_table = HashTable()
        data = ["".join([random_choice(ascii_letters) for _ in range(randint(1, 10))]) for _ in range(20)]
        self.__add_elems(hash_table, data)
        working_values = [elem for elem in hash_table]
        self.assertEqual(sorted(working_values), sorted(data))

    def test_remove(self):

        hash_table = HashTable(data=[1, 2, 3, 4, 5])

        for i in range(1, 6):
            self.assertEqual(hash_table.remove(i), True)
            self.assertEqual(hash_table.remove(5 + i), False)

        self.assertEqual(len(hash_table), 0)

        data = [1, 2, 3, 4, 6, 7, 10]
        hash_table = HashTable(data=[1, 6, 2, 7, 10, 3, 4])
        
        self.assertEqual(hash_table.remove(7), True)

        hash_table = HashTable(data=[(1, 2), (5, 6), (3, 4)], key=lambda x: x[0])
        self.assertEqual(hash_table.remove((1, 2)), True)
        self.assertEqual(hash_table.remove((3, 4)), True)

        self.assertEqual(sorted([elem for elem in hash_table]), [(5, 6)])

        self.assertEqual(hash_table.remove((5, 6)), True)
        self.assertEqual(len(hash_table), 0)

        data = [randint(0, 100) for _ in range(200)]
        hash_table = HashTable(data=data)
        self.__remove_elems(hash_table, data)

        data = ["".join([random_choice(ascii_letters) for _ in range(randint(1, 10))]) for _ in range(20)]
        hash_table = HashTable(data=data)
        self.__remove_elems(hash_table, data)

    def test_contains(self):

        data = [randint(0, 100) for _ in range(200)]
        hash_table = HashTable(data=data)

        for elem in data:
            self.assertEqual(hash_table.contains(elem), True)

        excluded_data = [randint(101, 1000) for _ in range(200)]
        for elem in excluded_data:
            self.assertEqual(hash_table.contains(elem), False)

        data = ["".join([random_choice(ascii_letters) for _ in range(randint(1, 10))]) for _ in range(20)]
        hash_table = HashTable(data=data)

        for elem in data:
            self.assertEqual(hash_table.contains(elem), True)

    def test_integration(self):

        random_data_size_1 = 100
        random_data_size_2 = 200

        hash_table = HashTable()
        data_1 = [randint(0, 100) for _ in range(random_data_size_1)] 
        data_2 = [randint(101, 1000) for _ in range(random_data_size_2)]

        self.__add_elems(hash_table, data_1)
        self.assertEqual(len(hash_table), len(set(data_1)))

        for elem in data_1:
            self.assertEqual(hash_table.contains(elem), True)

        for elem in data_2:
            self.assertEqual(hash_table.contains(elem), False)

        self.__add_elems(hash_table, data_2)
        self.assertEqual(len(hash_table), len(set(data_1 + data_2)))

        for elem in data_2:
            self.assertEqual(hash_table.contains(elem), True)

        self.assertEqual(sorted([elem for elem in hash_table]), sorted(set(data_1 + data_2)))
        self.assertEqual(len(hash_table), len(set(data_1 + data_2)))

        self.__remove_elems(hash_table, data_1)
        self.assertEqual(len(hash_table), len(set(data_2)))

        for elem in data_2:
            self.assertEqual(hash_table.contains(elem), True)

        for elem in data_1:
            self.assertEqual(hash_table.contains(elem), False)
            
        self.__remove_elems(hash_table, data_2)
        self.assertEqual(len(hash_table), 0)

    def __add_elems(self, hash_table, data):

        for elem in data:
            hash_table.add(elem)

    def __remove_elems(self, hash_table, data):

        starting_length = len(hash_table)

        for elem in set(data):
            self.assertEqual(hash_table.remove(elem), True)

        self.assertEqual(starting_length - len(hash_table), len(set(data)))
    

if __name__ == "__main__":
    unittest.main()
