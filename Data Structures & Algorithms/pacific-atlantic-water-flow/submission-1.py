class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #approach: add (r, c) for points that reach pac and another for atl, then res.append the ones that appear in both

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights [r][c] < prevHeight): #check bounds, if visited, and if it's shorter than its previous
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c]) #replace the prevheight, used as function passed value
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #top row -> touches the pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) #bottom row -> touches the atlanting

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        #now check that it appears in both
        res = []

        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])
        
        return res
        

