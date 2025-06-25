def solve(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        visited[r][c] = True
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows and
                0 <= nc < cols and
                not visited[nr][nc] and
                board[nr][nc] == 'O'
            ):
                dfs(nr, nc)

    for r in range(rows):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][cols - 1] == 'O':
            dfs(r, cols - 1)

    for c in range(cols):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[rows - 1][c] == 'O':
            dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and not visited[r][c]:
                board[r][c] = 'X'