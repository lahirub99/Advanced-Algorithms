"""
Basic Idea of the Approach 
• Iterate n times over matrix D, using index k 
• (k-1)th iteration: 
    D matrix has the solution where paths only contain vertices 1 to k-1 
• Next, in kth iteration: 
    compare the costs of 
    1.going from i to j using only vertices 1,…,k-1 (stored at dij in the (k-1)th iteration) 
    2.using the kth vertex as an intermediate step, which is dik (go from i to k) plus dkj (go from k to j)
    –Then remember the lower cost path
"""


def FloydWarshall(graph):
    # Initialize matrix with zeros
    dist = [[0 for x in range(V)] for y in range(V)]

    for i in range (0, V):
        for j in range (0, V):
            dist[i][j] = graph[i][j]
    
    for k in range (0, V):
        for i in range (0, V):
            for j in range (0, V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

### Test 01:
INFINITY, V = 99999, 4
# V = Number of vertices in the graph

graph = [[0, 5, INFINITY, 10], 
         [INFINITY, 0, 3, INFINITY],
         [INFINITY, INFINITY, 0, 1],
         [INFINITY, INFINITY, INFINITY, 0]]


print(FloydWarshall(graph))
