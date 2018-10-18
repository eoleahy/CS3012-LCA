# from BSTDAG import *
import networkx as nx
import unittest

class TestBSTMethods(unittest.TestCase):


    def lca(G,source,a,b):
        paths=nx.single_source_shortest_path(G,source,a)
        print("All path: ",  paths)
        pathA = paths[a]
        pathB = paths[b]
        print("path A: ", pathA)
        print("path B: ", pathB)

        lca = None

        for i in reversed(pathA):
            print("i", i)
            for j in reversed(pathB):
                print("j", j)
                if (i is j):
                    lca = i
                    print("LCA is", lca)
                    return(lca)
        return (lca)

    def setUp(self):
        pass

    def testLCA(self):
        G=nx.DiGraph()
        G.add_edge(1,2)
        G.add_edge(2,4)
        G.add_edge(4,3)
        G.add_edge(2,7)
        lca = TestBSTMethods.lca(G,1,3,7)
    #    print(paths)

        self.assertTrue(lca,2)
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
