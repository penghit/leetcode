class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize some list used for storing the adjacent list : adj
        # whether a node is on stack on one specfic depth search : onstack
        # whether a node has been visited : visited
        adj = [[] for _ in range(numCourses)]
        onstack = [0 for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        
        # Construct the adjacent list, for each i, adj[i] is all the nodes i points to
        for curr, pre in prerequisites:
            adj[pre].append(curr)
        
        res = [True]
        
        
        def dfs(v, res):
            onstack[v] = 1 # when entering a dfs(v), setting onstack[v] to true
            visited[v] = 1 # seeting visited [v] to true
            for w in adj[v]:
                if onstack[w] == 1:
                    res[0] = False
                if visited[w] == 0:
                    dfs(w, res)
            onstack[v] = 0 # when exiting a dfs(v), setting onstack[v] to false
        
        for v in range(numCourses):
            dfs(v, res)
                
        return res[0]
