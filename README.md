# README #

### What is this repository for? ###
This respiratory includes both an iterative and a recursive version of Floyd's algorithm and a performance test file to time both functions, the algorithm is used to determine the shortest paths between nodes in a weighted graph. 

* Version: 0.1

GitHub Repository: https://github.com/EvaG1312/floyds_algorithm

### How do I get set up? ###

1. Clone Repository: 
git clone https://github.com/EvaG1312/floyds_algorithm.git
cd floyds_algorithm

2.  Virtual Environment Setup (Optional):
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

.venv\Scripts\activate     # Windows


### Running the scripts ###

To execute the recursive version of Floyd's Algorithm: python src/recursion/recursive_floyd.py

To execute the iterative version of Floyd's Algorithm: python src/iterative/iterative_floyd.py

To compare the execution time of both implementations: python src/tests/performance_test.py
This will output execution times for 1000 iterations of each version

### Requirements ### 
Python 3.8+

no dependencies 

### Additional Notes ### 
The tested graph is randomly generated, so results may vary slightly each run; size is kept consistent (30) to get meaningful results 
The recursive version has a high recursion limit to prevent stack overflow 

Author: Eva Grieving (EvaG1312)
Last updated: 28/02/2025




