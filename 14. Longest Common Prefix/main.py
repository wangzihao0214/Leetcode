class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        
        n = len(strs[0])
        
        while i < n:
            target = strs[0][i]
            
            same = True
            for s in strs[1::]:
                l = len(s)
                if i == l:
                    return result
                if s[i] != target:
                    same = False
                    break
            
            if same:
                result += target
                i += 1
            else:
                return result
        
        return result