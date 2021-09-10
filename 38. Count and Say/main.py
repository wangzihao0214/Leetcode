class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        digit = "1"
        for i in range(2, n + 1):
            left = 0
            right = 0
            temp = ""
            
            while left < len(digit):
                if right < len(digit) and digit[right] == digit[left]:
                    right += 1
                else:
                    length = right - left
                    temp += str(length) + digit[left]
                    left = right
            digit = temp
        return digit