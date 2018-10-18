import networkx as nx
import unittest
import matplotlib.pyplot as plt

#This implementation is for a DAG that is not a Binary Search Tree
class TestMethods(unittest.TestCase):

    def lca(G,source,a,b):
        '''
        lca(G,source,a,b)
        @param(G): the graph containing the nodes and edges
        @param(source): the ancestor node
        @param(a): node you want to find ancestor of
        @param(b): the other node you want to find the ancestor of

        This function works by creating a dictionary of
        all lists representing paths in the Graph. It then finds the
        lists containing the paths from the source to the 2 parameter
        nodes. These lists are then reversed and iterated through to find
        the first occurence of a common node. This node is the LCA.
        '''

        paths=nx.single_source_shortest_path(G,source,a)
#        print("All path: ",  paths)
        pathA = paths[a]
        pathB = paths[b]
#        print("path A: ", pathA)
#        print("path B: ", pathB)
        lca = None

        for i in reversed(pathA):
            for j in reversed(pathB):
                if (i is j):
                    lca = i
#                    print("LCA is", lca)
                    return(lca)
        return (lca)

    def setUp(self):
        pass

    def testLCA(self):
        """  Model of Graph for this test
                1
               / \
              2
             / \
            4   7
           /
          3
        """
        G=nx.DiGraph()
        G.add_edge(1,2)
        G.add_edge(2,4)
        G.add_edge(4,3)
        G.add_edge(2,7)
        lca = TestMethods.lca(G,1,3,7)
        self.assertTrue(lca,2)

    def testLCA2(self):
        """  Model of Graph for this test
                1
               /|\
              4 5 3
               \ /
                7
        """
        G=nx.DiGraph()
        G.add_edge(1,4)
        G.add_edge(1,3)
        G.add_edge(1,5)
        G.add_edge(4,7)
        G.add_edge(3,7)
        lca = TestMethods.lca(G,1,5,7)
        self.assertTrue(lca,1)

    def testLCA3(self):
        """  Model of Graph for this test
                1
               /|\
              4 5 3
             / \ /
            2   7
        """
        G=nx.DiGraph()
        G.add_edge(1,4)
        G.add_edge(1,3)
        G.add_edge(1,5)
        G.add_edge(4,7)
        G.add_edge(4,2)
        G.add_edge(3,7)
        lca = TestMethods.lca(G,1,2,7)
        self.assertNotEqual(lca,3)

if __name__ == '__main__':
    unittest.main()
