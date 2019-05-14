class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check if each row is valid
        for i in range(9):
            digits = []
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in digits:
                        return False
                    digits.append(board[i][j])
        
        # check if each colomn is valid, difference from the previous one is
        # the first index for board is the second loop variable
        for i in range(9):
            digits = []
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in digits:
                        return False
                    digits.append(board[j][i])
           
        for i in [0,3,6]:
            for j in [0,3,6]:
                digits = []
                for m in range(0,3):
                    for n in range(0,3):
                        if board[i+m][j+n] != '.':
                            if board[i+m][j+n] in digits:
                                return False
                            digits.append(board[i+m][j+n])
        
        # if all checked finishied without return false, return true
        return True
