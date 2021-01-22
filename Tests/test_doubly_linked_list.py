import sys
sys.path.append(r"..")

import unittest
from Data_Structures.Source.doubly_linked_list import DoublyLinkedList


class TestLinkedList(unittest.TestCase):

    def test_constructor(self):

        l_list = DoublyLinkedList()
        l_list = DoublyLinkedList([1, 2, 3, 4, 5])
        l_list = DoublyLinkedList("some string")
        l_list = DoublyLinkedList(["some string"])
        l_list = DoublyLinkedList([[1, 2, 3], (4, 5)])

        with self.assertRaises(TypeError):
            l_list = DoublyLinkedList(1)

    def test_len(self):

        l_list = DoublyLinkedList()
        self.assertEqual(len(l_list), 0)

        l_list = DoublyLinkedList([1, 2, 3, 4, 5])
        self.assertEqual(len(l_list), 5)

        l_list = DoublyLinkedList("some string")
        self.assertEqual(len(l_list), 11)

        l_list = DoublyLinkedList(["some string"])
        self.assertEqual(len(l_list), 1)

        l_list = DoublyLinkedList([[1, 2, 3], (4, 5)])
        self.assertEqual(len(l_list), 2)

    def test_str(self):

        l_list = DoublyLinkedList()
        self.assertEqual(str(l_list), "[]")
        
        l_list = DoublyLinkedList([1, 2, 3, 4, 5])
        self.assertEqual(str(l_list), "[1, 2, 3, 4, 5]")

        l_list = DoublyLinkedList("some string")
        self.assertEqual(str(l_list), "['s', 'o', 'm', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']")

        l_list = DoublyLinkedList(["some string"])
        self.assertEqual(str(l_list), "['some string']")

        l_list = DoublyLinkedList([[1, 2, 3], (4, 5)])
        self.assertEqual(str(l_list), "[[1, 2, 3], (4, 5)]")

    def test_iter(self):
        
        l_list = DoublyLinkedList()
        generatedList = [elem for elem in l_list]
        self.assertEqual(str(l_list), str(generatedList))
        
        l_list = DoublyLinkedList([1, 2, 3, 4, 5])
        generatedList = [elem for elem in l_list]
        self.assertEqual(str(l_list), str(generatedList))

        l_list = DoublyLinkedList([[1, 2, 3], (4, 5)])
        generatedList = [elem for elem in l_list]
        self.assertEqual(str(l_list), str(generatedList))


    def __push_elems(self, l_list, elems, push_location="back"):

        starting_length = len(l_list)

        for elem in elems: 
            if push_location == "back": 
                l_list.push_back(elem)
            else:
                l_list.push_front(elem)

        self.assertEqual(len(l_list) - starting_length, len(elems))

    def test_push_back(self):

        l_list = DoublyLinkedList()

        test_list1 = [i for i in range(20)]
        self.__push_elems(l_list, test_list1)
        self.assertEqual(str(l_list), str(test_list1))
        
        test_list2 = [i for i in range(0, 20, -1)]
        self.__push_elems(l_list, test_list2)
        self.assertEqual(str(l_list), str(test_list1 + test_list2))

    def test_push_front(self):

        l_list = DoublyLinkedList()
        self.__push_elems(l_list, [i for i in range(20)], push_location="front")
        self.__push_elems(l_list, [i for i in range(0, 20, -1)], push_location="front")

    def test_pop_back(self):

        l_list = DoublyLinkedList()
        self.__push_elems(l_list, [i for i in range(20)])
        self.__pop_elems(l_list, [i for i in range(19, -1, -1)])

        with self.assertRaises(Exception):
            l_list.pop_back()

    def test_pop_front(self):

        l_list = DoublyLinkedList()
        self.__push_elems(l_list, [i for i in range(20)], push_location="front")
        self.__pop_elems(l_list, [i for i in range(19, -1, -1)], pop_location="front")

        with self.assertRaises(Exception):
            l_list.pop_front()

    def test_peek_back(self):

        l_list = DoublyLinkedList([1, 2, 3, 4, 5])
        
        for i in range(5, 0, -1):
            self.assertEqual(l_list.peek_back(), i)
            l_list.pop_back()

        with self.assertRaises(Exception):
            l_list.peek_back()

    def test_peek_front(self):

        l_list = DoublyLinkedList([1, 2, 3, 4, 5])
        
        for i in range(1, 6):
            self.assertEqual(l_list.peek_front(), i)
            l_list.pop_front()

        with self.assertRaises(Exception):
            l_list.peek_front()

    def __pop_elems(self, l_list, elems, pop_location="back"):

        starting_length = len(l_list)

        for i in range(0, len(elems)):
            if pop_location == "back": 
                self.assertEqual(l_list.pop_back(), elems[i])
            else:
                self.assertEqual(l_list.pop_front(), elems[i])

        self.assertEqual(len(l_list), starting_length - len(elems))     


if __name__ == "__main__":
    unittest.main()