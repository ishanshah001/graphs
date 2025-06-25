def findRedundantConnection(edges):
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)

        if rootX == rootY:
            return [x, y]
        
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

        return []

    parent = list(range(len(edges)+1))
    rank = [0] * (len(edges)+1)
    
    for e in edges:
        redudant = union(parent, rank, e[0], e[1])
        if redudant:
            return redudant

print(findRedundantConnection([[1,2],[1,3],[2,3]]))