class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #O(n2) to find 1, the bfs from island, change to 'X' to represent visited

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        numIslands = 0
        ROWS, COLS = len(grid), len(grid[0])

        #bfs runs if we find a "1"
        def bfs(r, c):
            q = deque()
            grid[r][c] = "X"
            q.append((r, c)) #tuple?

            #running bfs on neighbors of island
            while q:
                row, col = q.popleft() #this is why we need the tuple
                for dr, dc in directions: #check l u d r
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != "1"):
                        continue #what does this do
                    q.append((nr,nc))
                    grid[nr][nc] = "X"
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1
                    
        return numIslands
                        





            