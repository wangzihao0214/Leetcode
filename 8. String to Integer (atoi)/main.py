class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        other_list = [" ", "+", "-"]
        
        if len(s) == 0:
            return result
        
        if s[0] not in number_list and s[0] not in other_list:
            return result
        
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return result
        
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        
        if_start = False
        while  i < len(s):
            if s[i] == "0" and not if_start:
                i += 1
                if i >= len(s):
                    break
            
            if s[i] in number_list:
                if_start = True
                result = result * 10 + int(s[i])
                i += 1
            else:
                break
        
        result = result * sign
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result