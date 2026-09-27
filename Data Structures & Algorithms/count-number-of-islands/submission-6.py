class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                r, c = q.pop()
                grid[r][c] = "X"

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nc < 0 or nr<0 or nc >= COLS or nr >= ROWS or grid[nr][nc] != "1":
                        continue
                    
                    grid[nr][nc] = "X"
                    q.append((nr, nc))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
