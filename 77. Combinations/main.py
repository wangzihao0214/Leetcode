class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        path=[]
        
        def backtrace(n,k,startIndex):
            if len(path)==k:
                result.append(path[:])
                return 
            for i in range(startIndex,n+1):
                path.append(i)
                backtrace(n,k,i+1)
                path.pop()
        backtrace(n,k,1)
        return result

#         result = [[] for _ in range(k)]
        
#         for i in range(n):
#             result[0].append([i + 1])
        
#         for j in range(1, k):
#             for combination in result[j - 1]:
#                 for i in range(combination[-1], n):
#                     result[j].append(combination + [i + 1])
                        
#         return result[k - 1]
        