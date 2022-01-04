class Graph:
    
    # -------- initialization
    
    def __init__(self, colors):
        self.nodes = len(colors)
        self.adj = [[] for _ in range(self.nodes)]
        self.reset()
    
    # resets for new iteration
    
    def reset(self):
        self.visited = [False] * self.nodes
        self.recursion = [False] * self.nodes
        self.stack = []
        
    #reads in edges and then call addedge to append edges to neccesary nodes
        
    def addEdges(self, edges: List[List[int]]):
        for u,v in edges:
            self.addEdge(u, v)
        
    def addEdge(self, u, v):
        self.adj[u].append(v)   
        
        
    #==== DFS 
        
    def DFS(self, u):
        #if already been to node
        if self.recursion[u]:
            raise ValueError("Cycled Detected")
        
        #avoid as already visited

        if self.visited[u]:
            return

        #set as visited and indicate recursion from this point
        self.visited[u] = True
        self.recursion[u] = True
        
        #for each v adjacent to node
        
        for v in self.adj[u]:
            self.DFS(v)
         
        # return from recursion and append to stack
        self.stack.append(u)
            
        self.recursion[u] = False
    
    #creates new topological ordering
    
    def getTopological(self):        
        self.reset()
        
        for u in range(self.nodes):
            self.DFS(u)
        
        return self.stack[::-1]
    
    
    def getAdjs(self, u):
        return self.adj[u]
        
        

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        #initialize graph
        
        g = Graph(colors)
        g.addEdges(edges)
        
        try:
            #create topological ordering
            nodes = g.getTopological()

            result, arr = 0, [[0]*26 for _ in range(len(nodes))]
            for i in range(len(nodes)-1, -1, -1):       
                #selects node from found ordering
                
                u = nodes[i]
                
                # stores max color possibilty
                #creates 2d array of possible ordering * possible letters
                for v in g.getAdjs(u):
                    #letters in aplhabet
                    for l in range(26):
                        arr[u][l] = max(arr[u][l], arr[v][l])

                c = ord(colors[u])-97
                arr[u][c] += 1

                result = max(result, max(arr[u]))
            return result        
        except:
            return -1