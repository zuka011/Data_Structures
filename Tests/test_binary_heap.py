import sys

sys.path.append(r"..")

import unittest
from random import randint

from Source.binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def test_constructor(self):
        
        b_heap = BinaryHeap()
        b_heap = BinaryHeap([1, 2, 3, 4, 5])
        b_heap = BinaryHeap((1, 2, 3))
        b_heap = BinaryHeap([(3, 1), (1, 2), (5,)], lambda x: x[0])

        with self.assertRaises(TypeError):
            b_heap = BinaryHeap(1)

        with self.assertRaises(ValueError):
            b_heap = BinaryHeap((1, 2), 5)

    def test_len(self):

        b_heap = BinaryHeap()
        self.assertEqual(len(b_heap), 0)

        b_heap = BinaryHeap([1, 2, 3, 4, 5])
        self.assertEqual(len(b_heap), 5)

        b_heap = BinaryHeap((1, 2, 3))
        self.assertEqual(len(b_heap), 3)
        
        b_heap = BinaryHeap([(3, 1), (1, 2), (5,)], lambda x: x[0])
        self.assertEqual(len(b_heap), 3)

    def test_str(self):

        b_heap = BinaryHeap()
        self.assertEqual(str(b_heap), "[]")

        b_heap = BinaryHeap([1, 2, 3, 4, 5])
        self.assertEqual(str(b_heap), "[1, 2, 3, 4, 5]")

        b_heap = BinaryHeap((1, 2, 3))
        self.assertEqual(str(b_heap), "[1, 2, 3]")

        b_heap = BinaryHeap([(3, 1), (1, 2), (5,)], lambda x: x[0])
        self.assertEqual(str(b_heap), "[(1, 2), (3, 1), (5,)]")

    def test_iter(self):

        b_heap = BinaryHeap()
        working_values = [elem for elem in b_heap]
        self.assertEqual(working_values, [])

        b_heap = BinaryHeap([1, 2, 3, 4, 5])
        working_values = [elem for elem in b_heap]
        self.assertEqual(working_values, [1, 2, 3, 4, 5])

        b_heap = BinaryHeap((1, 2, 3))
        working_values = [elem for elem in b_heap]
        self.assertEqual(working_values, [1, 2, 3])

        b_heap = BinaryHeap([(3, 1), (1, 2), (5,)], lambda x: x[0])
        working_values = [elem for elem in b_heap]
        self.assertEqual(working_values, [(1, 2), (3, 1), (5,)])

    def test_push(self):

        b_heap = BinaryHeap()
        data = [randint(0, 100) for _ in range(200)]
        self.__push_elems(b_heap, data)
        working_values1 = [elem for elem in b_heap]

        b_heap = BinaryHeap()
        self.__push_elems(b_heap, data[::-1])
        working_values2 = [elem for elem in b_heap]

        self.assertEqual(working_values1, working_values2)

    def test_pop(self):

        data = [randint(0, 100) for _ in range(200)]
        b_heap = BinaryHeap(data)
        self.__pop_elems(b_heap, data)
        self.assertEqual(len(b_heap), 0)

        b_heap = BinaryHeap(data[::-1])
        self.__pop_elems(b_heap, data)
        self.assertEqual(len(b_heap), 0)

        with self.assertRaises(Exception):
            b_heap.pop()

    def test_peek(self):
        
        b_heap = BinaryHeap([1, 2, 3, 4, 5])
        
        for i in range(1, 6):
            self.assertEqual(b_heap.peek(), i)
            b_heap.pop()
        
        b_heap = BinaryHeap([(1, 2), (5, 6), (3, 4)], lambda x: x[0])
        
        for i in range(3):
            self.assertEqual(b_heap.peek()[1], i * 2)
            b_heap.pop()
        
        with self.assertRaises(Exception):
            b_heap.peek()
        
    def test_remove(self):

        b_heap = BinaryHeap([1, 2, 3, 4, 5])

        for i in range(1, 6):
            self.assertEqual(b_heap.remove(i), True)
            self.assertEqual(b_heap.remove(5 + i), False)

        self.assertEqual(len(b_heap), 0)

        b_heap = BinaryHeap([(1, 2), (5, 6), (3, 4)], lambda x: x[0])
        self.assertEqual(b_heap.remove((1, 2)), True)
        self.assertEqual(b_heap.remove((3, 4)), True)
        self.assertEqual(b_heap.remove((5, 7)), False)

        self.assertEqual([elem for elem in b_heap], [(5, 6)])

        self.assertEqual(b_heap.remove((5, 6)), True)
        self.assertEqual(len(b_heap), 0)

    def __push_elems(self, b_heap, data):

        elem_map = {}

        for elem in data:
            b_heap.push(elem)
            
            if elem not in elem_map: elem_map[elem] = 0
            elem_map[elem] += 1

        for elem in b_heap:
            elem_map[elem] -= 1

        for elem in elem_map:
            self.assertEqual(elem_map[elem], 0)

        working_values = [elem for elem in b_heap]
        self.assertEqual(sorted(working_values), working_values)


if __name__ == "__main__":
    unittest.main()
