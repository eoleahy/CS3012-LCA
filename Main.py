from BSTDAG import *
import networkx as nx
import unittest

class TestBSTMethods(unittest.TestCase):

    def setUp(self):
        pass

    def testInsert(self):
        print("Branch")
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
        x = tree.lca(tree.root,1,3)
        self.assertTrue(x, 2)

    def testLCA2(self):
        tree=Tree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(1)
        tree.insert(2)
        tree.insert(7)
        tree.insert(4)
        x = tree.lca(tree.root,2,4)
        self.assertTrue(x, 3)

if __name__ == '__main__':
    unittest.main()
