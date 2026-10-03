class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0,1], [0,-1]]
        visited = set()
        q = deque()
        dist = 0

        def helper(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                return
            
            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                for i,j in directions:
                    helper(i + r, j + c)
            
            dist += 1

