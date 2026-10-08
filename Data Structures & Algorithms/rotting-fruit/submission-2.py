class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        fresh = 0
        q = deque() #rotton fruit
        minutes = 0

        #bfs in layers ie in parallel

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        def helper(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r, c) in visited:
                return False
            return True

            
        while q:
            
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if helper(dr + r, dc + c):
                        q.append((dr + r, dc + c))
                        visited.add((dr + r, dc + c))
                        fresh -= 1
            if q: minutes += 1
        
        if fresh == 0: return minutes
        else: return -1


