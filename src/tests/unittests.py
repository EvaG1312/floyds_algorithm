import unittest
import sys

# Ensure modules are found
sys.path.append('../')  

# Import both versions 
import recursion.recursive_floyd as rf
import iterative.iterative_floyd as itf

class TestFloydsAlgorithm(unittest.TestCase):
    def setUp(self):
        """
        This method runs before each test.
        define a small known graph with known shortest-paths.
        """
        self.NO_PATH = sys.maxsize
        
        # Example 3x3 graph:
        # Distances:
        #   0 → 1 = 2
        #   1 → 2 = 3
        #   0 → 2 = 10 (but 0→1→2 is 2+3=5, so shorter path = 5)
        #   Diagonal = 0, 
        self.small_graph = [
            [0,    2,    10],
            [self.NO_PATH, 0,    3 ],
            [self.NO_PATH, self.NO_PATH, 0]
        ]

        # expected final distances:
        #   0→2 should be 5 (via 1)
        #   everything else remains the same or 0 for diagonal.
        self.expected_small_graph = [
            [0, 2, 5],
            [self.NO_PATH, 0, 3],
            [self.NO_PATH, self.NO_PATH, 0]
        ]

    def test_iterative_small_graph(self):
        """
        Overwrites the global GRAPH in iterative_floyd used for performance test
        runs algorithm and checks the final distances.
        """
        itf.GRAPH = [row[:] for row in self.small_graph]  #copy to avoid mutation issues
        itf.MAX_LENGTH = len(itf.GRAPH[0])

        itf.iterative_floyd()  #iterative version

        self.assertEqual(itf.GRAPH, self.expected_small_graph,
                         "Iterative final distances do not match expected results.")

    def test_recursive_small_graph(self):
        """
        Overwrites the global GRAPH in recursive_floyd,
        runs the algorithm, and checks the final distances.
        """
        rf.GRAPH = [row[:] for row in self.small_graph]  # Make a copy
        rf.MAX_LENGTH = len(rf.GRAPH[0])

        # recursive version starting from (0,0,0)
        rf.recursive_floyd_warshall(0, 0, 0)

        self.assertEqual(rf.GRAPH, self.expected_small_graph,
                         "Recursive final distances do not match expected results.")

if __name__ == '__main__':
    unittest.main()
