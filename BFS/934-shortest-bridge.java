class Solution {
    public int shortestBridge(int[][] A) {
        int m = A.length;
        int n = A[0].length;
        boolean[][] visited = new boolean[m][n];
        
        int[][] dirs = new int[][] {{-1,0}, {1,0}, {0,-1}, {0,1}};
        
        Queue<int[]> queue = new LinkedList<int[]>();
        
        for (int i=0; i<m*n; i++) {
            int r = i/m;
            int c = i%m;
            if (A[r][c] == 1) {
                dfs(A, visited, queue, r, c, dirs);
                break;
            }
        }
        
        //for (int[] cell : queue) System.out.println(cell[0] + " " + cell[1]);
        
        int step = 0;
        while (!queue.isEmpty()) {
            int s = queue.size();
            while (s > 0) {
                
                int[] cell = queue.poll();
                s--;
                for (int[] dir : dirs) {
                    int row = cell[0] + dir[0];
                    int col = cell[1] + dir[1];
                    if (row>=0 && row<m && col>=0 && col<n && !visited[row][col]) {
                        if (A[row][col] == 1) return step;
                        queue.add(new int[] {row, col});
                        visited[row][col] = true;
                    }
                }
            }
            step++;
        }
        
        
        return 0;
        
    }
    
    private void dfs(int[][] A, boolean[][] visited, Queue<int[]> queue, int r, int c, int[][] dirs) {
        int m = A.length;
        int n = A[0].length;
        if (r<0 || r>=m || c<0 || c>=n || visited[r][c] || A[r][c] == 0) return;
        visited[r][c] = true;
        queue.add(new int[] {r, c});
        
        for (int[] dir : dirs) {
            dfs(A, visited, queue, r+dir[0], c+dir[1], dirs);
        }
    }
    

}
