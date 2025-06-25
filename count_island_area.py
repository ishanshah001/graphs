def maxAreaOfIsland(grid):
    if not grid:
        return 0
        
    count = 0
    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count = dfs(grid, i, j)
                max_count = max(max_count, count)
    return max_count

def dfs( grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
        return 0
    count = 1
    grid[i][j] = 'V'
    count+= dfs(grid, i+1, j)
    count+= dfs(grid, i-1, j)
    count+= dfs(grid, i, j+1)
    count+= dfs(grid, i, j-1)
    return count