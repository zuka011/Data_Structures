import sys

sys.path.append(r"..")

import unittest

from Source.union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_constructor(self):
        
        u_find = UnionFind()
        u_find = UnionFind(10)
        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        u_find = UnionFind(["cat", "dog", [1, 2]])

    def test_len(self):

        u_find = UnionFind()
        self.assertEqual(len(u_find), 0)
        
        u_find = UnionFind(10)
        self.assertEqual(len(u_find), 10)

        u_find = UnionFind(3, [1, 2, 3, 4, 5])
        self.assertEqual(len(u_find), 5)

        u_find = UnionFind(10, [1, 2, 3, 4, 5])
        self.assertEqual(len(u_find), 10)

        u_find = UnionFind(["cat", "dog", [1, 2]])
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

        u_find = UnionFind(["cat", "dog", [1, 2]])
        self.assertEqual(str(u_find), "[('cat', 1), ('dog', 2), ([1, 2], 3)]")

    def test_iter(self):

        pass
    

if __name__ == "__main__":
    unittest.main()
