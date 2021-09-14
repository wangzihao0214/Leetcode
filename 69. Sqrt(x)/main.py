class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while True:
            mid = (left + right) // 2
            if mid * mid > x:
                if (mid - 1) * (mid - 1) <= x:
                    return mid - 1
                else:
                    right = mid
            elif mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                elif (mid + 1) * (mid + 1) == x:
                    return mid + 1
                else:
                    left = mid
            else:
                return mid