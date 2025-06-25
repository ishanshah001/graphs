def countComponents(n, edges):
    def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)

        if rootX == rootY:
            return
        
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        parent = [find(parent, i) for i in range(n)]
        return

    parent = list(range(n))
    rank = [0] * (n)
    
    for e in edges:
        union(parent, rank, e[0], e[1])
    
    return len(set(parent))

n=6
edges=[[0,1],[2,3],[4,5],[1,2],[3,4]]
print(countComponents(n, edges))