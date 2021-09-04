class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        n = len(s)
        result = 0
        
        i = 0
        while i < n:
            if s[i] == "I":
                if i < n - 1 and s[i + 1] == "V":
                    result += 4
                    i += 2
                elif i < n - 1 and s[i + 1] == "X":
                    result += 9
                    i += 2
                else:
                    result += 1
                    i += 1
            elif s[i] == "X":
                if i < n - 1 and s[i + 1] == "L":
                    result += 40
                    i += 2
                elif i < n - 1 and s[i + 1] == "C":
                    result += 90
                    i += 2
                else:
                    result += 10
                    i += 1
            elif s[i] == "C":
                if i < n - 1 and s[i + 1] == "D":
                    result += 400
                    i += 2
                elif i < n - 1 and s[i + 1] == "M":
                    result += 900
                    i += 2
                else:
                    result += 100
                    i += 1
            else:
                result += dic[s[i]]
                i += 1
        
        return result
            