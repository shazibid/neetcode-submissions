class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #1. find the first 0 (bfs)
        #2. check l r u d for another 0
            #a. if 0 is found, recurse check, bfs
            #b. if all 4 are X, 0 -> X
            #c. if at the edge, leave the 0 alone

        
        ROWS, COLS = len(board), len(board[0])
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #takes no input??
        def bfs():
            queue = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    #checking if it's near bounds
                    if (r == 0 or r == ROWS - 1
                        or c == 0 or c == COLS - 1
                    ) and board[r][c] == "O":
                        queue.append((r, c)) #tuple
            
            while queue:
                r, c = queue.popleft()
                
                #revaluing to show visited, will be changed later
                if board[r][c] == "O":
                    board[r][c] = "S"
                    #bfs to find all neighbors
                    for dr, dc in d:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            queue.append((nr, nc))
            
        bfs()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

        






