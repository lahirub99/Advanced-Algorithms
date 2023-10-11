
"""
Part 3:
    Develop a more time-efficient algorithm than the algorithm in (a) above, using 
    dynamic programming or memoization concepts. Present your idea clearly.
"""
def count_paths_dp(m, n):
    # Create a 2D array to store path counts
    dynamic_array = [[1] * n] * m

    # Iterate through the dynamic_array
    for i in range(1, m):
        for j in range(1, n):
            # Calculate the number of paths to reach (i, j)
            dynamic_array[i][j] = dynamic_array[i-1][j] + dynamic_array[i][j-1]

    # Return the count of paths from (1, 1) to (m, n)
    return dynamic_array[m-1][n-1]

# Example usage
m = 3
n = 3
print(count_paths_dp(m, n))  # Output: 6

"""
Part 4:
    What is the time-complexity of your algorithm in (c) above?
Answer:
    The time complexity of the algorithm in (c) above is O(m*n) because the algorithm
    iterates through the dynamic_array m*n times.
"""