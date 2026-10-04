class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0],[0,1], [0,-1]]
        dist = 0
        q = deque()
        visited = set()

        def helper(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == -1 or (r, c) in visited:
                return
            
            q.append((r, c))
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
    
        while q:
            for _ in range(len(q)): #why do we have this for loop in the while loop
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:

                    helper(r + dr, dc + c)

            dist += 1
        

