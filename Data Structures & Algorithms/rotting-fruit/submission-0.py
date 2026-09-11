class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source bfs
        #minute
            #bfs from each
        

        #need to find the rotten first
        queue = collections.deque() #array of indices
        fresh = 0
        timer = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j)) #we want the position of the rotten
        
        d = [[1, 0], [-1,0], [0,1], [0,-1]]
        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()

                #checking all neighbors for rotten
                for dr, dc in d:
                    r2, c2 = r + dr, c + dc

                    if (r2 in range(len(grid)) 
                        and c2 in range(len(grid[0]))
                        and grid[r2][c2] == 1):
                        grid[r2][c2] = 2
                        queue.append((r2, c2))
                        fresh -= 1
            timer += 1
        
        return timer if fresh == 0 else -1