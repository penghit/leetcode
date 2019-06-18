class Solution {
    
    public class Cell implements Comparable<Cell>{
        int row;
        int col;
        int height;
        public Cell(int row, int col, int height) {
            this.row = row;
            this.col = col;
            this.height = height;
        }
        
        public int compareTo(Cell that) {
            return this.height - that.height;
        }
    }
    
    
    public int trapRainWater(int[][] heightMap) {
        
        int res = 0;
        
        if (heightMap == null || heightMap.length == 0) return 0;
        
        int m = heightMap.length;
        int n = heightMap[0].length;
        
        if (m <= 2 || n <= 2) return 0;
        
        boolean[][] visited = new boolean[m][n];
        PriorityQueue<Cell> pq = new PriorityQueue<Cell>();
        
        for (int i=0; i<m; i++) {
            pq.offer(new Cell(i, 0, heightMap[i][0]));
            pq.offer(new Cell(i, n-1, heightMap[i][n-1]));
            visited[i][0] = true;
            visited[i][n-1] = true;
        }
        
        for (int i=0; i<n; i++) {
            
            if (!visited[0][i]) {
                pq.offer(new Cell(0, i, heightMap[0][i]));
                visited[0][i] = true;
            }
            if (!visited[m-1][i]) {
                pq.offer(new Cell(m-1, i, heightMap[m-1][i]));
                visited[m-1][i] = true;
            }
        }
        
        //System.out.println(pq.poll().height);
        //System.out.println(pq.poll().height);
        //System.out.println(pq.poll().height);
        //System.out.println(pq.poll().height);
        
        int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        while (!pq.isEmpty()) {
            Cell cell = pq.poll();
            for (int[] d : dirs) {
                int r = cell.row + d[0];
                int c = cell.col + d[1];
                if (r>=0 && r<m && c>=0 && c<n && !visited[r][c]) {
                    visited[r][c] = true;
                    res = res + Math.max(0, cell.height - heightMap[r][c]);
                    pq.offer(new Cell(r, c, Math.max(cell.height, heightMap[r][c])));
                }
            }
        }
        
        
        
        return res;
        
    }
}
