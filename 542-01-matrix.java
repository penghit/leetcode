class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        //System.out.println(m + " " + n);
        
        Queue<int[]> queue = new LinkedList<> ();
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (matrix[i][j] == 0)
                    queue.add(new int[] {i, j});
                else
                    matrix[i][j] = Integer.MAX_VALUE;
                    
            }
        }
        
        //for (int[] abc : queue) System.out.println(abc[0] + " " + abc[1]);
        
        int[][] direction = {{-1,0},{1,0},{0,-1},{0,1}};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            for (int[] d : direction) {
                int row = curr[0] + d[0];
                int col = curr[1] + d[1];
                if (row<0 || row>=m || col<0 || col >=n || matrix[row][col] <= matrix[curr[0]][curr[1]]) continue;
                matrix[row][col] = matrix[curr[0]][curr[1]] + 1;
                queue.add(new int[] {row,col});
                    
            }
        }

        
        return matrix;
        
    }
}
