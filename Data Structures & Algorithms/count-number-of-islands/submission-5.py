class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "X"

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    
                    if nr >= ROWS or nc >= COLS or nr < 0 or nc <0 or grid[nr][nc] != "1":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "X"
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands
