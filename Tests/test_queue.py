import sys
sys.path.append(r"..")

import unittest
from Data_Structures.queue import Queue


class TestQueue(unittest.TestCase):

    def test_constructor(self):
        
        queue = Queue()
        queue = Queue([1, 2, 3, 4, 5])
        queue = Queue("some string")
        queue = Queue(["some string"])
        queue = Queue(["This", "is", ["a", "test"]])

        with self.assertRaises(TypeError):
            queue = Queue(1)

    def test_len(self):

        queue = Queue()
        self.assertEqual(len(queue), 0)

        queue = Queue([1, 2, 3, 4, 5])
        self.assertEqual(len(queue), 5)
        
        queue = Queue("some string")
        self.assertEqual(len(queue), 11)

        queue = Queue(["some string"])
        self.assertEqual(len(queue), 1)

        queue = Queue(["This", "is", ["a", "test"]])
        self.assertEqual(len(queue), 3)

    def test_str(self):

        queue = Queue()
        self.assertEqual(str(queue), "[]")

        queue = Queue([1, 2, 3, 4, 5])
        self.assertEqual(str(queue), "[1, 2, 3, 4, 5]")

        queue = Queue("some string")
        self.assertEqual(str(queue), "['s', 'o', 'm', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']")

        queue = Queue(["some string"])
        self.assertEqual(str(queue), "['some string']")

        queue = Queue(["This", "is", ["a", "test"]])
        self.assertEqual(str(queue), "['This', 'is', ['a', 'test']]")

    def test_iter(self):
        
        queue = Queue()
        generatedList = [elem for elem in queue]
        self.assertEqual(str(queue), str(generatedList))
        
        elems = [1, 2, 3, 4, 5]
        queue = Queue(elems)
        generatedList = [elem for elem in queue]
        self.assertEqual(str(elems), str(generatedList))

        elems = [[1, 2, 3], (4, 5)]
        queue = Queue(elems)
        generatedList = [elem for elem in queue]
        self.assertEqual(str(elems), str(generatedList))

    def test_push(self):

        queue = Queue()

        test_elems1 = [i for i in range(20)]
        self.__push_elems(queue, test_elems1)
        self.assertEqual(str(queue), str(test_elems1))
        
        test_elems2 = [i for i in range(10, 0, -1)]
        self.__push_elems(queue, test_elems2)
        self.assertEqual(str(queue), str((test_elems1 + test_elems2)))

    def __pop_elems(self, queue, elems):

        starting_length = len(queue)

        for i in range(len(elems)): 
            self.assertEqual(queue.dequeue(), elems[i])

        self.assertEqual(starting_length - len(queue), len(elems))

    def test_pop(self):

        test_elems1 = [i for i in range(20)]
        queue = Queue(test_elems1)

        self.__pop_elems(queue, test_elems1)

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_peek(self):

        test_elems1 = [i for i in range(20)]
        queue = Queue(test_elems1)

        test_elems1 = test_elems1

        for i in range(len(test_elems1)):
            self.assertEqual(queue.peek(), test_elems1[i])
            queue.dequeue()

        with self.assertRaises(Exception):
            queue.peek()

    def __push_elems(self, queue, elems):

        starting_length = len(queue)

        for elem in elems: 
            queue.enqueue(elem)

        self.assertEqual(len(queue) - starting_length, len(elems))

if __name__ == "__main__":
    unittest.main()