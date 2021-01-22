import sys
sys.path.append(r"..")

import unittest
from Data_Structures.Source.stack import Stack


class TestStack(unittest.TestCase):

    def test_constructor(self):
        
        stack = Stack()
        stack = Stack([1, 2, 3, 4, 5])
        stack = Stack("some string")
        stack = Stack(["some string"])
        stack = Stack(["This", "is", ["a", "test"]])

        with self.assertRaises(TypeError):
            stack = Stack(1)

    def test_len(self):

        stack = Stack()
        self.assertEqual(len(stack), 0)

        stack = Stack([1, 2, 3, 4, 5])
        self.assertEqual(len(stack), 5)

        stack = Stack("some string")
        self.assertEqual(len(stack), 11)

        stack = Stack(["some string"])
        self.assertEqual(len(stack), 1)

        stack = Stack(["This", "is", ["a", "test"]])
        self.assertEqual(len(stack), 3)

    def test_str(self):

        stack = Stack()
        self.assertEqual(str(stack), "[]")

        stack = Stack([1, 2, 3, 4, 5])
        self.assertEqual(str(stack), "[5, 4, 3, 2, 1]")

        stack = Stack("some string")
        self.assertEqual(str(stack), "['g', 'n', 'i', 'r', 't', 's', ' ', 'e', 'm', 'o', 's']")

        stack = Stack(["some string"])
        self.assertEqual(str(stack), "['some string']")

        stack = Stack(["This", "is", ["a", "test"]])
        self.assertEqual(str(stack), "[['a', 'test'], 'is', 'This']")

    def test_iter(self):

        stack = Stack()
        generatedList = [elem for elem in stack]
        self.assertEqual(str(stack), str(generatedList))
        
        elems = [1, 2, 3, 4, 5]
        stack = Stack(elems)
        generatedList = [elem for elem in stack]
        self.assertEqual(str(elems[::-1]), str(generatedList))

        elems = [[1, 2, 3], (4, 5)]
        stack = Stack(elems)
        generatedList = [elem for elem in stack]
        self.assertEqual(str(elems[::-1]), str(generatedList))

    def __push_elems(self, stack, elems):

        starting_length = len(stack)

        for elem in elems: 
            stack.push(elem)

        self.assertEqual(len(stack) - starting_length, len(elems))

    def test_push(self):

        stack = Stack()

        test_elems1 = [i for i in range(20)]
        self.__push_elems(stack, test_elems1)
        self.assertEqual(str(stack), str(test_elems1[::-1]))
        
        test_elems2 = [i for i in range(10, 0, -1)]
        self.__push_elems(stack, test_elems2)
        self.assertEqual(str(stack), str((test_elems1 + test_elems2)[::-1]))

    def test_pop(self):

        test_elems1 = [i for i in range(20)]
        stack = Stack(test_elems1)

        self.__pop_elems(stack, test_elems1[::-1])

        with self.assertRaises(Exception):
            stack.pop()

    def test_peek(self):

        test_elems1 = [i for i in range(20)]
        stack = Stack(test_elems1)

        test_elems1 = test_elems1[::-1]

        for i in range(len(test_elems1)):
            self.assertEqual(stack.peek(), test_elems1[i])
            stack.pop()

        with self.assertRaises(Exception):
            stack.peek()
            
    def __pop_elems(self, stack, elems):

        starting_length = len(stack)

        for i in range(len(elems)): 
            self.assertEqual(stack.pop(), elems[i])

        self.assertEqual(starting_length - len(stack), len(elems))


if __name__ == "__main__":
    unittest.main()