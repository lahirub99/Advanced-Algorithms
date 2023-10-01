""" Input to the test cases:
    Graph: Network with edge capacities.
    
Example:
        
Grpaph = [[0, 7, 0, 0, 5, 0],
        [0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 1, 6, 0, 0],
        [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5
"""

# Breadth First Search (BFS) algorithm
# returns True if an s-t path exists; pred contains the path as a predcessor list
# returns False if no s-t path exists
def breadth_first_search(graph, source, sink, pred):
    visited = [False] * (len(graph))
    queue = []

    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for index, val in enumerate(graph[u]):
            if (visited[index] == False) and (val > 0):
                queue.append(index)
                visited[index] = True
                pred[index] = u
    return visited[sink]

# Ford Fulkerson Algorithm
def ford_fulkerson(residualGraph, source, sink):
    # pred[] contains the path as a predecessor list
    pred = [-1] * (len(residualGraph))
    max_flow = 0 # There is no flow initially

    while breadth_first_search(residualGraph, source, sink, pred):  # find augmenting path
        # initialize the flow along augmenting path as infinity
        path_flow = float("Inf")
        s = sink

        # Find the flow along augmenting path
        while(s != source):
            path_flow = min(path_flow, residualGraph[pred[s]][s])
            s = pred[s]
        
        # Augment the residual network to update residual capacities
        max_flow += path_flow

        # We use the residual network to update the residual capacities
        v = sink
        while(v != source):
            u = pred[v]
            residualGraph[u][v] -= path_flow
            residualGraph[v][u] += path_flow
            v = pred[v]
            
    return max_flow