class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}

        stk = []
        for p in s[::-1]:
            if p not in dic:
                stk += p
            else:
                if len(stk) == 0:
                    return False
                temp = stk.pop()
                if dic[p] != temp:
                    return False
                
        if len(stk) == 0:
            return True
        else:
            return False