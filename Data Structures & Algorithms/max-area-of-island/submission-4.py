class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        maxarea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 0

            while q:
                r, c = q.pop()
                area += 1

                for dr,dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue #next values in for loop
                    
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxarea = max(maxarea, area)
        
        return maxarea

                    