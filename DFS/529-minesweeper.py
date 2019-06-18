class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:


        adj = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board 


        def dfs(board, r, c, adj):
            count = 0
            #print("before", count)
            if board[r][c] != 'E':
                return
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            for cell in adj:
                nr, nc = r + cell[0], c + cell[1]
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                    if board[nr][nc] == 'M':
                        count = count + 1
            #print("after", count)
            if count == 0:
                board[r][c] = 'B'
            else:
                board[r][c] = str(count)
                return
            for cell in adj:
                nr, nc = r + cell[0], c + cell[1]
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                    dfs(board, nr, nc, adj)
                    
                    
        #print(row, col)
        dfs(board, row, col, adj)
        
        return board
