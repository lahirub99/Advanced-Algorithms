"""
###--- Breadth-first search Psuedo Code ---###

# white  - Unvisited
# gray   -  Discovered
# black  - Finished

# s - Source Vertex
# Q - FIFO Queue 

BFS(G, s):
    for each vertex u in V[G]-{s}:
        set Color[u] = white  
        set Distance[u] = ∞  
        set Parent[u] = nil 
    set Color[s] = gray 
    set Distance[s] = 0 
    set Parent[s] = nil 
    set Q = {s} 
    
    while Q ≠ Ø:
        set u = Head[Q]  
        for each v in Adj[u]:
            if Color[v] == white:
                set Color[v] = gray
                set Distance[v] = Distance[u] + 1
                set Parent[v] = u
                Enqueue(Q,v)
        Dequeue(Q)
        set Color[u] = black
"""

def BreadthFirstSearch(G, s): # G is the graph given as an adjacency list, s is the source vertex
    Color = {} # white, gray, black
    Distance = {} # distance from source vertex
    Parent = {} # parent of each vertex

    for vertex in G.keys():
        Color[vertex] = 'white'
        Distance[vertex] = float('inf')
        Parent[vertex] = None

    Color[s] = 'gray'
    Distance[s] = 0
    Parent[s] = None
    Q = [s]

    while len(Q) != 0:
        u = Q[0]
        for v in G[u]:
            if Color[v] == 'white':
                Color[v] = 'gray'
                print(v,"is discovered. Parent is",u)

                Distance[v] = Distance[u] + 1   # Considering the graph as a tree
                Parent[v] = u
                Q.append(v)
                print(Color, "Queue:", Q)

        Q.pop(0)
        Color[u] = 'black'
    print(Color)
    print(Distance)
    print(Parent)


# A sample graph implemented as an adjacency list
Graph = {'A': ['B', 'C', 'E'],
         'B': ['F'],
         'C': ['G'],
         'D': ['A'],
         'E': [],
         'F': [],
         'G': [],
         'H': ['F']
        }


BreadthFirstSearch(Graph, 'A')