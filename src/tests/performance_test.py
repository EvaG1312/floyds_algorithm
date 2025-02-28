"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
sys.path.append('../')
from recursion.recursive_floyd import recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd
from time import process_time

def performance_test(function_handle, iterations=1000, size=50):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters

       iterations -> times the function should run to get an average 
    """
    total_time = 0
    for _ in range(iterations):
        start_time = process_time()
        function_handle()  # Run the algorithm no parameters
        end_time = process_time()
        total_time += (end_time - start_time)

    avg_time = total_time / iterations
    print(f"Execution time over {iterations} iterations: {avg_time:.6f} seconds")
    

print ("Recursion Test Time")
performance_test(lambda: recursive_floyd_warshall(0, 0, 0))

print ("Iterative Test Time")
performance_test(iterative_floyd)
    


