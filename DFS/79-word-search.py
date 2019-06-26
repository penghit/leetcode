class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        row = len(board)
        col = len(board[0])
        
        def dfs(board, i, j, word, word_index):
            if len(word) - 1 == word_index:
                return True
            board[i][j] = ""
            #print(board[i][j])
            for r, c in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if r>=0 and r<row and c>=0 and c<col and board[r][c] == word[word_index+1] and dfs(board, r, c, word, word_index+1):
                    #print(word[word_index+1])
                    return True
                
            board[i][j] = word[word_index]
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(board, i, j, word, 0):
                    return True
                
        return False
    
