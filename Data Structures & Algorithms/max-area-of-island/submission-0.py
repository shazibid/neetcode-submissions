class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        maxcnt = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #if 0, next, if 1, check right, down, left, up for other ones, bfs
                if grid[r][c] == 1:
                    count = 0
                    queue = deque([(r, c)])
                    grid[r][c] = 0 #mark as visited
                    
                    #check in a while loop for every side
                    while queue:
                        i, j = queue.popleft()
                        count += 1
                        
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni, nj = i + dr, j + dc
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                                grid[ni][nj] = 0
                                queue.append((ni, nj))
                        #while queue, push, then pop and check and pop and check
                    
                    maxcnt = max(maxcnt, count)
            
        return maxcnt
