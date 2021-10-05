class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):return -1
        n = len(cost)
        for i in range(n):          
            tank = 0
           
            for j in range(n):
                k = (i + j) % n          
                tank += gas[k] - cost[k]
      
                if tank < 0:break
            else:              
                return i
                
        return -1
