class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        x = str(x)
        sign = 1
        if x[0] == "-":
            sign = -1
            x = x[1::]
        x = x[::-1]
        while x[0] == "0":
            x = x[1::]
        if sign == -1:
            x = "-" + x
        x = int(x)
        
        if x < -2**31 or x > 2**31 - 1:
            return 0
        
        return x