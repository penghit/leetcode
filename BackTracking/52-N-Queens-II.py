class Solution:
    def totalNQueens(self, n: int) -> int:
        
        
        def isSafe(row, col):
            return not (cols[col] + hill_diag[row - col] + dale_diag[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diag[row - col] = 1
            dale_diag[row + col] = 1
            
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diag[row - col] = 0
            dale_diag[row + col] = 0
            
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
            
        
        def dfs(row):
            for col in range(n):
                if isSafe(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        dfs(row + 1)
                    remove_queen(row, col)
                    
        cols = [0] * n
        hill_diag = [0] * 2 * n
        dale_diag = [0] * 2 * n
        queens = set()
        output = []
        dfs(0)
        return len(output)
