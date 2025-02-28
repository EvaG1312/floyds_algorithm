"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd_warshall -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
import sys
sys.setrecursionlimit(500000)  # Increasing recurstion limits for performance test results

import random
from sys import maxsize

NO_PATH = maxsize
SIZE = 30  # matrix change for meaningful results 

# Generate a random  matrix with distances (1-20), keeping diagonal as 0
GRAPH = [[random.randint(1, 20) if i != j else 0 for j in range(SIZE)] for i in range(SIZE)]

MAX_LENGTH = SIZE  # Update MAX_LENGTH dynamically
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

def main():
    """
    This is the calling function for the recursive floyd's algorithm
    """
    # function call to recursive_floyd_warshall needs to be here
    
    recursive_floyd_warshall (0, 0, 0)
    print_out_graph()

    #uncomment next line when you have completed the task
    

def print_out_graph():
    """
    This function prints out the graph with the distances
    and a place holder for no path between nodes
    """
    for start_node in range(0,MAX_LENGTH):
        for end_node in range(0,MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER 

            message = "Distance from Node %s to Node %s is %s" %\
                (start_node,end_node,distance)
            print (message)
def recursive_floyd_warshall(outer_loop:int, middle_loop:int, inner_loop:int):
        """
        This function computes shortest path between each pair node
        It computes by comparing a direct path with paths that have 
        intermediate nodes in the path.

        The recursive path is the shortest path function which
        calls itself to find the shortest path between a pair of nodes

        You need to increment each variable until it reaches a loop

        param: outer_loop: This variable is from the first loop of the iterative version
        param: middle_loop: This variable is from the second loop of the iterative version
        param: inner_loop: This variable is from the last loop of the iterative version
        """
    # establishing base case
        if outer_loop == MAX_LENGTH:
            return # stops when complete
        
      # when middle_loop reached end -> to next intermediate node 
        if middle_loop == MAX_LENGTH:
            recursive_floyd_warshall(outer_loop + 1,0,0)
            return
        
    # when inner_loop reached end -> to next source node
        if inner_loop == MAX_LENGTH:
            recursive_floyd_warshall(outer_loop, middle_loop + 1,0)
            return
    
        
    # Updating current element in Floyds
        GRAPH[middle_loop][inner_loop] = min(
        GRAPH[middle_loop][inner_loop],
        GRAPH[middle_loop][outer_loop] + GRAPH[outer_loop][inner_loop])
    
    # moving to next object in row within the function
        recursive_floyd_warshall(outer_loop, middle_loop, inner_loop + 1)
    

if __name__ == "__main__":
    main()
