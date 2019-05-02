class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        
        Map<Integer, List<int[]>> graph = new HashMap<> ();
        
        for (int[] time : times) {
            if (!graph.containsKey(time[0])) {
                graph.put(time[0], new ArrayList<int[]>());
            }
            graph.get(time[0]).add(new int[] {time[1], time[2]});
        }
        
        //System.out.println(graph.get(2).get(1)[0]);
        
        PriorityQueue<int[]> pq = new PriorityQueue<> ((e1, e2) -> e1[0] - e2[0]);
        
        /* test priority queue
        pq.offer(new int[] {0, 2});
        pq.offer(new int[] {4, 3});
        pq.offer(new int[] {2, 4});
                
        System.out.println(pq.poll()[0]);
        System.out.println(pq.poll()[0]);
        */
        
        pq.offer(new int[] {0, K});
        
        Map<Integer, Integer> dist = new HashMap();
        

        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int d = info[0];
            int node = info[1];
            if (dist.containsKey(node)) continue;
            dist.put(node,d);
            if (graph.containsKey(node)) {
                for (int[] edge : graph.get(node)) {
                    int nei = edge[0];
                    int d2 = edge[1];
                    if (!dist.containsKey(nei))
                        pq.offer(new int[] {d + d2, nei});
                }
            }
        }
        
        if (dist.size() != N) return -1;
        
        int res = 0;
        
        for (int d : dist.values()) {
            res = Math.max(d, res);
        }
        
        
        
        return res;
    }
    
    
    
    
    
}
