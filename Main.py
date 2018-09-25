from BST import *
import unittest

class TestBSTMethods(unittest.TestCase):

    def setUp(self):
        pass

    def testInsert(self):
        tree=Tree()
        tree.insert(5)
        self.assertEqual(tree.getRoot().val,5)

    def testInsert2(self):
        tree=Tree()
        tree.insert(3)
        self.assertFalse(tree.getRoot().val==5)

    def testEmpty(self):
        tree=Tree()
        self.assertTrue(tree.isEmpty())

    def testLCA(self):
        tree=Tree()
        tree.insert(2)
        tree.insert(3)
        tree.insert(1)
        tree.insert(5)
        tree.insert(7)
        tree.insert(1)
        self.assertTrue(tree.getRoot().val,2)
        self.assertTrue(tree.lca(tree.getRoot(), 1, 3) == 2)

if __name__ == '__main__':
    unittest.main()
