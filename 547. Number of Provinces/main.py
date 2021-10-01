class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = 0
        
        visited = [False] * n
        s = []
        
        for i in range(n):
            if not visited[i]:
                s.append(i)
                visited[i] = True
                while len(s):
                    source = s.pop()
                    for j in range(n):
                        if isConnected[source][j] == 1 and not visited[j]:
                            s.append(j)
                            visited[j] = True
                result += 1
        
        return result
                    