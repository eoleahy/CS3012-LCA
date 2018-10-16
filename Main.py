# from BSTDAG import *
import networkx as nx
import unittest

class TestBSTMethods(unittest.TestCase):


    def lca(G,source,a,b):
        pathA=nx.single_source_shortest_path(G,source,a)
        pathB=nx.single_source_shortest_path(G,source,b)

        return (pathA)

    def setUp(self):
        pass

    def testLCA(self):
        G=nx.DiGraph()
        G.add_edge(1,2)
        G.add_edge(2,3)
        G.add_edge(2,7)
        paths = TestBSTMethods.lca(G,1,3,7)
        print(paths)
        x=3
        self.assertTrue(3,3)
"""
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
"""


if __name__ == '__main__':
    unittest.main()
