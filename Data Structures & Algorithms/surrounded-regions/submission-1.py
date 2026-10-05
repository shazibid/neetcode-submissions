class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #check if its by a boarder
        #if by boarder, bfs to turn all neighbors into seen
        #then in main turn back to O and turn all other O into X cus captured

        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        #1. check borders
        #2. dfs from found point and add points to visited, DO NOT CHANGE
        #3. go through grid and check if X or if in visited, if not visited and O, change to X

        #2
        def dfs(r, c, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O" or (r, c) in visited:
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited)

        #1
        for r in range(ROWS):
            dfs(r, 0, visited)
            dfs(r, COLS - 1, visited)
        for c in range(COLS):
            dfs(0, c, visited)
            dfs(ROWS - 1, c, visited)
        
        #3
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"