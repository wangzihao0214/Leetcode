class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        length = len(p)
        result = []
        
        dic = {}
        remain = 0
        for i in range(length):
            dic[p[i]] = dic.get(p[i], 0) + 1
            remain += 1
        
        if length > n:
            return result
        
        left = 0
        pointer = 0
        while left <= n - length:
            if dic.get(s[pointer]):
                dic[s[pointer]] -= 1
                remain -= 1
                pointer += 1
            else:
                if s[left] in dic.keys():
                    dic[s[left]] += 1
                    remain += 1
                    left += 1
                else:
                    left += 1
                    pointer = left
            if remain == 0:
                result.append(left)
                dic[s[left]] += 1
                remain += 1
                left += 1
        
        return result
                