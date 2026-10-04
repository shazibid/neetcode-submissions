class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        minutes = 0
        count = 0

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    count += 1

        def helper(r, c):
            nonlocal count
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r, c) in visited:
                return
            
            q.append((r, c))
            visited.add((r, c))
            count -= 1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    helper(r + dr,dc + c)
            if q:
                minutes += 1
                
            
        
        if count == 0: return minutes
        else: return -1