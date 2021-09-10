class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n == 0 or n == 1:
            return 0

        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
            right[n-i-1] = max(right[n-i], height[n-i-1])

        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - height[i]

        return res
    
#         n = len(height)
#         result = 0
#         d = []
#         for i in range(n - 1):
#             d.append(height[i + 1] - height[i])
        
#         n = len(d)
#         left = 0
#         while left < n -1:
#             if d[left] < 0:
#                 pivot = left
#                 right = left + 1
#                 while right < n and d[right] < 0:
#                     right += 1
#                 if right == n:
#                     if d[right - 1] > 0:
#                         pivot = right + 1
#                     else:
#                         left += 1
#                         continue
#                 else:
#                     pivot = right + 1
#                     while right < n and height[pivot] < height[left]:
#                         if height[right + 1] > height[pivot]:
#                             pivot = right + 1
#                         right += 1
#                 print(left, right, pivot)     
#                 result += min(height[left], height[pivot]) * (pivot - left - 1)
#                 for i in range(left + 1, pivot):
#                         result -= min(height[i], height[pivot])
#                 left = pivot
#             else:
#                 left += 1
        
#         return result
