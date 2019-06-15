class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        
        List<Integer> leaves = new ArrayList<> ();
        if (n == 1) {
            leaves.add(0);
            return leaves;
        }
        if (n == 2) {
            leaves.add(0);
            leaves.add(1);
            return leaves;
        }
        
        List<Set<Integer>> adj = new ArrayList<> ();
        
        for (int i=0; i<n; i++) {
            adj.add(new HashSet<> ());
        }
        
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        
        //System.out.println(adj);
        
        for (int i=0; i<n; i++) {
            if (adj.get(i).size() == 1) leaves.add(i);
        }
        
        //System.out.println(leaves);
        
        while (n > 2) {
            n = n - leaves.size();
            List<Integer> newleaves = new ArrayList<> ();
            for (int i : leaves) {
                int j = adj.get(i).iterator().next();
                adj.get(j).remove(i);
                if (adj.get(j).size() == 1) newleaves.add(j);
            }
            leaves = newleaves;
        }
        
        return leaves;
    }
}
