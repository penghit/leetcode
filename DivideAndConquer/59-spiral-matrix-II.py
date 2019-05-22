class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # very similar procedure to problem spiral matrix, but instead
        # of taking values from an matrix, we assign values to a matrix
        ans = [[0] * n for _ in range(n)]
        
        r = 0
        c = 0
        di = 0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        for i in range(n*n):
            ans[r][c] = i+1
            
            nextr = r + dr[di]
            nextc = c + dc[di]
            if nextr>=0 and nextr<n and nextc>=0 and nextc<n and ans[nextr][nextc]==0:
                r, c = nextr, nextc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        
        return ans
