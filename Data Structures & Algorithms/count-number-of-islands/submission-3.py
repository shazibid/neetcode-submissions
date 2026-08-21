class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ## bfs
                    #move on when all child nodes == 0
                    queue = deque([[i,j]])

                    count += 1
                    
                    #if value == 1, add to queue,
                    while queue:
                        [p, q] = queue.popleft() #going to put i,j in p,q
                        grid[p][q] = "X"

                        if p < len(grid) - 1 and grid[p + 1][q] == "1":
                            queue.append([p+1, q])
                            grid[p+1][q] = "X"
                        if q < len(grid[0]) - 1 and grid[p][q+1] == "1":
                            queue.append([p, q+1])
                            grid[p][q+1] = "X"
                        if p > 0 and grid[p - 1][q] == "1":
                            queue.append([p-1, q])
                            grid[p-1][q] = "X"
                        if q > 0 and grid[p][q-1] == "1":
                            queue.append([p, q-1])
                            grid[p][q-1] = "X"

        return count
               
