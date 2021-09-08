class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        s1 = list(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        dic = {}
        for char in s1:
            dic[char] = dic.get(char, 0) + 1
        dic_temp = dic.copy()

        left = 0
        right = 0
        while left <= n2 - n1:
            while right < left + n1 and right < n2:
                if s2[right] in dic_temp.keys():
                    if dic_temp[s2[right]] > 0:
                        dic_temp[s2[right]] -= 1
                        right += 1
                    else:
                        dic_temp[s2[left]] += 1
                        left += 1
                else:
                    dic_temp = dic.copy()
                    left = right + 1
                    right = left
            if right - left == n1:
                return True

        return False
