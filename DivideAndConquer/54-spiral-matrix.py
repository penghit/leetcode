class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        
        visited = [[False]*col for _ in range(row)]
        
        #print(visited)
        r = 0
        c = 0
        #direction for the next move, 0 means right, 1 means down, 2 means left, 3 means up
        di = 0
        # dr, dc means the number should be added to the current row and col given the direction
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        for i in range(row * col):
            ans.append(matrix[r][c])
            visited[r][c] = True
            nextr = r + dr[di]
            nextc = c + dc[di]
            if nextr >=0 and nextr < row and nextc >=0 and nextc < col and not visited[nextr][nextc]:
                r, c = nextr, nextc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        
        return ans
