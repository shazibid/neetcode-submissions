class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #count number of 1's seen
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxA = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            area = 1

            while q:
                r, c = q.popleft()
                grid[r][c] = 0


                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxA = max(maxA, area)
        
        return maxA

