"""
Given a matrix of size 𝑚 × 𝑛 where the rows are numbered 1,2,…,𝑚 and
the columns are numbered 1,2,…,𝑛 , let us consider the problem of counting all the 
possible paths from the top-left cell (1,1) to the bottom-right cell (𝑚, 𝑛) with the 
constraint that from each cell you can only move either to right (→) or down (↓). 

Part 1: 
    Develop a basic recursive algorithm to count the paths from the top-left cell (1,1)
    to the bottom-right cell (𝑚, 𝑛), assuming 𝑚 and 𝑛 are given as inputs. (Do not 
    worry about the efficiency of this basic algorithm. You are expected to improve its 
    efficiency later).
"""

def count_paths(m,n):
    if m==1 or n==1:
        # Assumed that if the matrix is 1x1 there is 1 path
        return 1
    else:
        # Number of paths to the cell (𝑖,𝑗) can be computed using the number of paths to its left neighbor cell (𝑖,𝑗 − 1) and top neighbor cell (𝑖 − 1,𝑗).
        # paths to left neighbor cell (𝑖,𝑗 − 1) = count_paths(i, j-1)
        # paths to top neighbor cell (𝑖 − 1,𝑗)  = count_paths(i-1, j)
        return count_paths(m-1,n) + count_paths(m,n-1)
    
# Test:
#print(count_paths(2,3))
#print(count_paths(2,2))

"""
Part 2:
    What is the time-complexity of your algorithm in (a) above? 
Answer:
    The time complexity of the algorithm in (a) above is O(2^(m+n-2)) because the algorithm
    is a recursive algorithm that calls itself twice. 
    The algorithm will run until it reaches the base case (m==1 or n==1) and the number of 
    recursive calls is 2^(m+n-2) - 1
        T(m,n) = O(2^(m+n-2)) //
"""
