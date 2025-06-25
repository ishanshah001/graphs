from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    visited = {}
    return dfs(node, visited)

def dfs(current_node, visited):

    if current_node in visited:
        return visited[current_node]

    cloned_node = Node(current_node.val)
    visited[current_node] = cloned_node

    for neighbor in current_node.neighbors:
        cloned_node.neighbors.append(dfs(neighbor, visited))

    return cloned_node