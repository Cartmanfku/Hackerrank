
class undirected_graph(object):
    
    def __init__(self, V):
        self.adj = [list() for i in range(0, V)]
        self.degree = [0 for i in range(0, V)]
        self.V = V
        self.E = 0
    
    def V(self):
        return self.V
    
    def E(self):
        return self.E
    
    def add_edge(self,v,u):
        self.adj[v].append(u)
        self.adj[u].append(v)
        self.degree[v] = self.degree[v] + 1
        self.degree[u] = self.degree[u] + 1
        self.E = self.E+1
        
    def get_adj(self,v):
        return self.adj[v]
    
    def get_degree(self,v):
        return self.degree[v]
        
    
def count(g, v, p, c):
    for u in g.get_adj(v):
        if u == p:
            continue
        count(g,u,v,c)
        c[v] = c[v] + c[u]
    
    
           
            
            
V,E = map(int,raw_input().split(' '))
g = undirected_graph(V)
for i in range(0,E):
    v,u = map(int,raw_input().split(' '))
    g.add_edge(v-1, u-1)

c = [1 for i in range(0,V)]
count(g,0,None,c)
cut = 0
for x in c[1:]:
    if x%2 == 0:
        cut = cut + 1 
        
print cut
