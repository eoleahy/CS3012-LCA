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

if __name__ == '__main__':
    unittest.main()
