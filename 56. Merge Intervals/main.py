class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(interval, low, high):
            if interval[1] < low or interval[0] > high:
                return False
            return True
        
        n = len(intervals)
        dp = [[] for _ in range(n)]
        dp[0].append(intervals[0])
        
        for i in range(1, n):
            dp[i].append(intervals[i])
            for interval in dp[i - 1]:
                low, high = dp[i][0][0], dp[i][0][1]
                if overlap(interval, low, high):
                    dp[i][0][0] = min(interval[0], low)
                    dp[i][0][1] = max(interval[1], high)
                else:
                    dp[i].append(interval)  
            print(dp[i])
        return dp[n - 1]