class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node_cur, path):
            if node_cur == n - 1:
                self.result.append(path[:])
                return
            for node in graph[node_cur]:
                path.append(node)
                dfs(node, path)
                path.pop()
        
        n = len(graph)
        self.result = []
        dfs(0, [0])
        
        return self.result
    