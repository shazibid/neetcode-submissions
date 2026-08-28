class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #shortest path to 0 and avoiding -1
        land = 2147483647
        #start from treasure, then bfs
        #update treasure to min(curr, distance)

        #iterate until first treasure is found
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                #find first treasure
                if grid[r][c] == 0:
                    #bfs on nearby islands
                    queue = deque([(r, c, 0)])
                    while queue:
                        (i, j, distance) = queue.popleft()
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                            
                            ni, nj = i + di, j + dj #gives us all l, r, u, d
                            
                            if ni < len(grid) and ni >=0 and nj < len(grid[0]) and nj >= 0:
                                if grid[ni][nj] > distance + 1:
                                    #update value in place based on distance
                                    queue.append((ni, nj, distance + 1)) #appending indexes of neighbors
                                    grid[ni][nj] = distance + 1
        
                            





        