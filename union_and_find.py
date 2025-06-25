def initialize(n):
    parent = list(range(n))
    rank = [0] * n
    return parent, rank

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    # already in same component
    if rootX == rootY:
        return False
    
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1
    # parent = [find(parent, i) for i in range(n)]
    return True

n = 5
parent, rank = initialize(5)

print(parent)
print(rank)

union(parent, rank, 4, 2)
union(parent, rank, 2, 3)
union(parent, rank, 1, 4)

print(find(parent, 3))
print(parent)