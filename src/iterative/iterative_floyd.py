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
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
import random
from sys import maxsize
from itertools import product

NO_PATH = maxsize
SIZE = 30  # Making sure size the same as in recursive_floyd.py so performance test results are meaningful 


# Generate a random  matrix with distances (1-20), keeping diagonal as 0
GRAPH = [[random.randint(1, 20) if i != j else 0 for j in range(SIZE)] for i in range(SIZE)]

MAX_LENGTH = SIZE  
NO_PATH_MARKER = "No Path"


def main():
    """
    This is the calling function for the recursive floyd's algorithm
    """
    iterative_floyd()
    print_out_graph()

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


def iterative_floyd():
    """
    A simple implementation of Floyd's algorithm.
    There is a nested loop which uses product to compute
    the possible combinations of the loops. This is for
    neater code 
    """
    for intermediate, start_node,end_node\
    in product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        
           if start_node == end_node:
               GRAPH[start_node][end_node] = 0
               continue
           
           GRAPH[start_node][end_node] = min(GRAPH[start_node][end_node],
                                 GRAPH[start_node][intermediate] + GRAPH[intermediate][end_node] )       
if __name__ == "__main__":
    main()
