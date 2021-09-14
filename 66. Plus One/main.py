class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        flag = 1
        
        for i in range(n):
            digits[-1 - i] = flag + digits[-1 - i]
            if digits[-1 - i] == 10:
                flag = 1
                digits[-1 - i] = 0
                if i == n - 1:
                    digits[0] = 0
                    digits = [1] + digits
                    flag = 0
            else:
                flag = 0
            if not flag:
                break
                
        return digits