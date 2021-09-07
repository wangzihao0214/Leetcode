class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result =  dividend // divisor
        if result != dividend / divisor:
            if result < 0:
                result += 1
        if result < - 2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result