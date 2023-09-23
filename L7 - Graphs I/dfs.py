
"""
###--- Depth-first search Psuedo Code ---###

# White - undiscovered, Gray - discovered, Black - finished

DFS(G): 
    for each vertex u in V[G]:
        set Color[u] = white 
        set Parent[u] = nil 
    
    for each vertex u in V[G] 
        if Color[u] == white  
            DFS_Visit(u) 

DFS_Visit(u):
    set Color[u] = gray 
    for each vertex v in Adj[u]  
        if Color[v] == white: 
            set Parent[v] = u
            DFS_Visit(v) 
    Color[u] = black
"""

# Time: O(V + E) - V is the number of vertices and E is the number of edges
# Space: O(V) - V is the number of vertices

def DepthFirstSearch(G): # G is the graph given as an adjacency list
    Color = {} # white, gray, black
    Parent = {} # parent of each vertex

    for vertex in G.keys():
        Color[vertex] = 'white'
        Parent[vertex] = None

    for vertex in G.keys():
        if Color[vertex] == 'white':
            DFS_Visit(vertex, G, Color, Parent)
            # Color and Parent are declared inside the DepthFirstSearch function and passed as arguments to the DFS_Visit function.
            # Othewise, they would have to be declared as global variables outside the fuctions.
    print(Color)
    print(Parent)

def DFS_Visit(Vertex, Graph, Color, Parent):
    Color[Vertex] = 'gray'  # Vertex has been discovered
    print(Vertex,"is discovered. Parent is",Parent[Vertex])
    for v in Graph[Vertex]: # For each neighbor of Vertex
        if Color[v] == 'white': # If that particular vertex is not discovered yet
            #print(v,"is discovered. Parent is",Vertex)
            Parent[v] = Vertex
            DFS_Visit(v, Graph, Color, Parent)    # Recursively visit each neighbor and mark each and their neighbors as discovered
            print(Color)
    Color[Vertex] = 'black' # Vertex has been finished


# A sample graph implemented as an adjacency list
Graph = {'A': ['B', 'C', 'E'],
         'B': ['F'],
         'C': ['G'],
         'D': ['A'],
         'E': [],
         'F': ['H'],
         'G': [],
         'H': []
        }

DepthFirstSearch(Graph)
